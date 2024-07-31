test_run_data=/home/admini/Documents/shoreline-pipeline/images/coastsat/test_run_data
mountthis=/home/admini/Documents/shoreline-pipeline/images/coastsat/mountThis
branch=dev/update-save-path-handling


startDate="2024-06-01" 
endDate="2024-07-01"
savePath="run_data/intersects/2024-06-01_2024-07-01_data.csv"
# coordinates="[[-125.895220405324,49.1237726477147], 
#         [-125.88841138016,49.1127817966321],  
#         [-125.899425059767,49.1098655680256], 
#         [-125.906924940215,49.1205546121385], 
#         [-125.895220405324,49.1237726477147]]"
sitename="CHESTERMANN"
epsg="3005"
transects="/run_data/input/transects.geojson"
tides="/run_data/tides/20240601_20240701_tides.csv"
ref_shoreline="/run_data/input/ref_shoreline.pkl"

# docker run -it \
#         -v $test_run_data:/data \
#         -v $mountthis:/sampleRunner \
#         --entrypoint /bin/bash \
#         coastsat

docker run -it \
        -v $test_run_data:/run_data \
        coastsat \
        $startDate $endDate $savePath \
        "[[-125.895220405324,49.1237726477147],[-125.88841138016,49.1127817966321],[-125.899425059767,49.1098655680256],[-125.906924940215,49.1205546121385],[-125.895220405324,49.1237726477147]]" \
        $sitename \
        $epsg $transects $tides $ref_shoreline \
        $branch
