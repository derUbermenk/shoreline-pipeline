# ECS Cluster
resource "aws_ecs_cluster" "ecs_cluster" {
  name = "shoreline-pipeline-cluster"

  tags = {
    Name = "shoreline-pipeline"
  }
}

# IAM Role for ECS Instances
resource "aws_iam_role" "ecs_instance_role" {
  name = "ecsInstanceRole"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "ec2.amazonaws.com"
      }
    }]
  })

  tags = {
    Name = "shoreline-pipeline"
  }
}

# Attach AmazonEC2ContainerServiceforEC2Role policy to the instance role
resource "aws_iam_role_policy_attachment" "ecs_instance_policy_attach" {
  role       = aws_iam_role.ecs_instance_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role"
}

# Create an IAM Instance Profile
resource "aws_iam_instance_profile" "ecs_instance_profile" {
  name = "ecsInstanceProfile"
  role = aws_iam_role.ecs_instance_role.name

  tags = {
    Name = "shoreline-pipeline"
  }
}

# Launch Configuration for ECS Instances
resource "aws_launch_template" "ecs_launch_template" {
  name_prefix   = "ecs-launch-template"
  image_id      =  data.aws_ami.ecs_optimized.id # ECS optimized AMI
  instance_type = "t2.micro"

  key_name = aws_key_pair.shoreline_auth.key_name

  iam_instance_profile {
    name = aws_iam_instance_profile.ecs_instance_profile.name
  }

  vpc_security_group_ids = [aws_security_group.shoreline_public_sg.id]

  user_data = filebase64("${path.module}/ecs.sh")
}

# Create an Auto Scaling Group to manage EC2 instances
resource "aws_autoscaling_group" "ecs_asg" {
  desired_capacity     = 0
  max_size             = 1 
  min_size             = 0
  vpc_zone_identifier  = [aws_subnet.shoreline_ecs_subnet.id]
  launch_template {
    id      = aws_launch_template.ecs_launch_template.id
    version = "$Latest"
  }
  health_check_type         = "EC2"
  health_check_grace_period = 300

  tag {
    key                 = "AmazonECSManaged"
    value               = true
    propagate_at_launch = true
  }

  tag {
    key                 = "Name"
    value               = "shoreline-asg"
    propagate_at_launch = false
  }
}

resource "aws_ecs_cluster_capacity_providers" "shoreline_cluster_capacity_provider" {
  cluster_name       = aws_ecs_cluster.ecs_cluster.name
  capacity_providers = [aws_ecs_capacity_provider.shorline_capacity_provider.name]

 default_capacity_provider_strategy {
   base              = 1
   weight            = 100
   capacity_provider = aws_ecs_capacity_provider.shorline_capacity_provider.name

 }
}

resource "aws_ecs_capacity_provider" "shorline_capacity_provider" {
  name = "shorline_capacity_provider"

  auto_scaling_group_provider {
    auto_scaling_group_arn         = aws_autoscaling_group.ecs_asg.arn 

    managed_scaling {
      maximum_scaling_step_size = 1 
      minimum_scaling_step_size = 1
      status                    = "ENABLED"
      target_capacity           = 5
    }
  }
}

# Get ECS Optimized AMI (depends on the region)
data "aws_ami" "ecs_optimized" {
  most_recent = true

  filter {
    name   = "name"
    values = ["amzn2-ami-ecs-hvm-*-x86_64-ebs"]
  }

  owners = ["amazon"]  # Amazon ECS AMI owner
}

resource "aws_ecs_task_definition" "grabtide" {
  family = "grabtide"
  container_definitions = jsonencode([
    {
      name      = "grabtide-container"
      image     = "yearningalpaca/grabtide:latest"
      cpu       = 10
      memory    = 300 
      essential = true
    }
  ])
}
