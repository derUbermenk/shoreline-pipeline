import datetime
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount 

chm_bc_coastline_pipeline = DAG(
    dag_id="chm_bc_coastline_pipeline",
    description = "pseudo sends emails. just saves to csv",
    start_date=datetime.datetime(2024, 1, 1),
    end_date=datetime.datetime(2024, 6, 1),
    schedule_interval="@daily"
)

grabtide = DockerOperator(
    task_id = "grabtide",
    image = "grabtide",
    dag=chm_bc_coastline_pipeline,
    command = [
        "{{ds_nodash}}",
        "{{next_ds_nodash}}",
        "/output",
        "9440083"
    ],
    mounts = [
        Mount(source="./data/9440083/input", target="/output", type="bind"),
    ]
)

coastsat = DockerOperator(
    task_id = "coastsat",
    image = "coastsat",
    dag=chm_bc_coastline_pipeline,
    command = [
        "{{ds}}",
        "{{next_ds}}",
        "/output",
        "[[-125.895220405324,49.1237726477147], \
        [-125.88841138016,49.1127817966321],  \
        [-125.899425059767,49.1098655680256], \
        [-125.906924940215,49.1205546121385], \
        [-125.895220405324,49.1237726477147]]",
        "CHESTERMANN",
        "3005",
        "/output/transects.geojson",
        "/output/tides.csv",
        "/output/ref_shoreline.pkl"
    ],
    mounts = [
        Mount(source="./data/9440083/input", target="/input", type="bind"),
        Mount(source="./data/9440083/output", target="/output", type="bind"),
    ]
)

grabtide >> coastsat