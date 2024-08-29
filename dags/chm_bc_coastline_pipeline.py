import datetime
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount 

chm_bc_coastline_pipeline = DAG(
    dag_id="chm_bc_coastline_pipeline",
    description = "coastline tracking for Chesterman beach, British Columbia, Canada",
    start_date=datetime.datetime(2024, 1, 1),
    end_date=datetime.datetime(2024, 6, 1),
    schedule_interval="@monthly"
)

grabtide = DockerOperator(
    task_id = "grabtide",
    image = "grabtide",
    dag=chm_bc_coastline_pipeline,
    command = [
        "{{ds_nodash}}",
        "{{next_ds_nodash}}",
        "/tides",
        "9440083",
        "main"
    ],
    # mounts = [
    #     Mount(source="/home/admini/Documents/shoreline-pipeline/data/9440083/input", target="/output", type="bind"),
    # ]
    volumes = [
    "/home/admini/Documents/shoreline-pipeline/data/chesterman_bc_9440083/tides:/tides"
    ]
)

coastsat = DockerOperator(
    task_id = "coastsat",
    image = "coastsat",
    dag=chm_bc_coastline_pipeline,
    command = [
        "{{ds}}",
        "{{next_ds}}",
        "CHESTERMANN"
        "3005",
        "/tides/{{ds_nodash}}_{{next_ds_nodash}}_tides.csv",
        "postgresql://shoreline:shoreline@shoreline_db:5432/shoreline",
        "dev/add-sql-support"
    ],
    network_mode="shoreline-pipeline_default",
    environment={
        'SERVICE_ACCOUNT_EMAIL': 'sat-img-dl@satimagedownloader.iam.gserviceaccount.com'
    },
    volumes = [
    "/home/admini/Documents/shoreline-pipeline/data/chesterman_bc_9440083/tides:/tides"
    ]
)

parse_intersects = DockerOperator(
    task_id = 'parse_intersects',
    image = 'shoreline-intersect-parser',
    dag = chm_bc_coastline_pipeline,
    command = [
        "/input/transects.geojson",
        "/intersects/{{ds}}_{{next_ds}}_data.csv",
        "/segments/{{ds}}_{{next_ds}}_segments.geojson",
        "main"
    ],
    volumes = [
        "/home/admini/Documents/shoreline-pipeline/data/chesterman_bc_9440083/input:/input",
        "/home/admini/Documents/shoreline-pipeline/data/chesterman_bc_9440083/intersects:/intersects",
        "/home/admini/Documents/shoreline-pipeline/data/chesterman_bc_9440083/segments:/segments"
    ] 
)

grabtide >> coastsat # >> parse_intersects