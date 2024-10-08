
test_run_data=/home/admini/Documents/shoreline-pipeline/images/coastsat/test_run_data

startDate="2024-06-01" 
endDate="2024-07-01"
sitename="CHESTERMAN"
epsg="3005"
tides="/run_data/tides/20240601_20240701_tides.csv"
connstring="postgresql://shoreline:shoreline@shoreline_db:5432/shoreline"
# branch="dev/add-sql-support"
branch="dev/add-sql-support"

docker run -it \
    -v $test_run_data:/run_data \
    --network shoreline-pipeline_default \
    coastsat \
    $startDate \
    $endDate \
    $sitename \
    $epsg \
    $tides \
    $connstring \
    $branch
