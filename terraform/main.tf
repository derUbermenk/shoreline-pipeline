resource "aws_vpc" "shoreline_vpc" {
  cidr_block           = "10.123.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name = "dev"
  }
}

resource "aws_subnet" "shoreline_public_subnet" {
  vpc_id                  = aws_vpc.shoreline_vpc.id
  cidr_block              = "10.123.1.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "us-west-2a"

  tags = {
    Name = "shoreline-dev-public_subnet"
  }
}

resource "aws_internet_gateway" "shoreline_internet_gateway" {
  vpc_id = aws_vpc.shoreline_vpc.id 

  tags = {
    Name = "shoreline-dev-igw"
    Environment = var.dev_resource_environment
  }
}

resource "aws_route_table" "shoreline_public_route_table" {
  vpc_id = aws_vpc.shoreline_vpc.id

  tags = {
    Name = "shoreline-dev-public_rt"
    Environment = var.dev_resource_environment
  }
}

resource "aws_route" "internet_route" {
  route_table_id         = aws_route_table.shoreline_public_route_table.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.shoreline_internet_gateway.id
}

resource "aws_route_table_association" "shoreline_public_route_table_assoc" {
  subnet_id      = aws_subnet.shoreline_public_subnet.id
  route_table_id = aws_route_table.shoreline_public_route_table.id
}

resource "aws_security_group" "shoreline_public_sg" {
  name        = "dev_sg"
  description = "dev security group"
  vpc_id      = aws_vpc.shoreline_vpc.id

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = var.allowed_ingress_ips
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_key_pair" "shoreline_auth" {
  key_name   = "shoreline_key"
  public_key = file("~/.ssh/shoreline_auth.pub")
}

resource "aws_instance" "airflow_server" {
  instance_type          = "t2.micro"
  ami                    = data.aws_ami.server_ami.id
  vpc_security_group_ids = [aws_security_group.shoreline_public_sg.id]
  subnet_id              = aws_subnet.shoreline_public_subnet.id
  user_data              = file("userdata.tpl")
  // setting key name 
  // can also use id, as they are the same when running
  // terraform state show aws_key_pair.mtc_auth
  // key_name = aws_key_pair.mtc_auth.id
  key_name = aws_key_pair.shoreline_auth.key_name

  tags = {
    Name = "shoreline-dev-airflow-server"
    Environment = var.dev_resource_environment
  }
}

resource "aws_s3_bucket" "shoreline_bucket" {
  bucket= "shoreline-bucket-randomadobe"

  tags = {
    Name        = "Shoreline bucket"
    Environment = var.dev_resource_environment
  }
}
