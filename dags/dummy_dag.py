import datetime
from airflow import DAG
from airflow.providers.amazon.aws.operators.ecs import EcsRunTaskOperator 

dummy_dag = DAG(
    dag_id="dummy_dag",
    description = "dag for trying to run tasks on ecs operators and s3",
    start_date=datetime.datetime(2024, 1, 1),
    end_date=datetime.datetime(2024, 1, 2),
    schedule_interval="@monthly"
)

ecs_task = EcsRunTaskOperator(
    task_id="ecs_task",
    dag=dummy_dag,
    # aws_conn_id="shoreline_ingestion",
    # cluster="shoreline-pipeline-cluster",
    cluster="arn:aws:ecs:us-west-2:710543700077:cluster/shoreline-pipeline-cluster",
    task_definition="arn:aws:ecs:us-west-2:710543700077:task-definition/grabtide:1", # grabtide
    launch_type="EC2",
    overrides={
        "containerOverrides": [
            {
                "name": "grabtide-container",
                "command": [
                    "{{ds_nodash}}", 
                    "{{next_ds_nodash}}",
                    "/tides",
                    "9440083",
                    "shoreline-bucket-randomadobe",
                    "tides/test_run.csv"
                ],
            }
        ]
    },
    region_name="us-west-2",
)

# grabtide = DockerOperator(
#     task_id = "grabtide",
#     image = "grabtide",
#     dag=chm_bc_coastline_pipeline,
#     command = [
#         "{{ds_nodash}}",
#         "{{next_ds_nodash}}",
#         "/tides",
#         "9440083",
#         "main"
#     ],
#     # mounts = [
#     #     Mount(source="/home/admini/Documents/shoreline-pipeline/data/9440083/input", target="/output", type="bind"),
#     # ]
#     volumes = [
#     "/home/admini/Documents/shoreline-pipeline/data/chesterman_bc_9440083/tides:/tides"
#     ]
# )

ecs_task