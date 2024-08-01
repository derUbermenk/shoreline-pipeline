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
        "/intersects/{{ds}}_{{next_ds}}_data.csv",
        "[[-125.895220405324,49.1237726477147],[-125.88841138016,49.1127817966321],[-125.899425059767,49.1098655680256],[-125.906924940215,49.1205546121385],[-125.895220405324,49.1237726477147]]",
        "CHESTERMANN",
        "3005",
        "/input/transects.geojson",
        "/tides/{{ds_nodash}}_{{next_ds_nodash}}_tides.csv",
        "/input/ref_shoreline.pkl",
        "master"
    ],
    environment={
        'SERVICE_ACCOUNT_EMAIL': 'sat-img-dl@satimagedownloader.iam.gserviceaccount.com'
    },
    # mounts = [
    #     Mount(source="/home/admini/Documents/shoreline-pipeline/data/9440083/input", target="/input", type="bind"),
    #     Mount(source="/home/admini/Documents/shoreline-pipeline/data/9440083/output", target="/output", type="bind"),
    # ]
    volumes = [
    "/home/admini/Documents/shoreline-pipeline/data/chesterman_bc_9440083/input:/input",
    "/home/admini/Documents/shoreline-pipeline/data/chesterman_bc_9440083/tides:/tides",
    "/home/admini/Documents/shoreline-pipeline/data/chesterman_bc_9440083/intersects:/intersects"
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

grabtide >> coastsat >> parse_intersects