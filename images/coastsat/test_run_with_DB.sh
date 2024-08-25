
test_run_data=/home/admini/Documents/shoreline-pipeline/images/coastsat/test_run_data
startDate="2024-06-01" 
endDate="2024-07-01"
sitename="CHESTERMAN"
epsg="3005"
tides="/run_data/tides/20240601_20240701_tides.csv"
connstring="postgresql://shoreline:shoreline@localhost:5436/shoreline_db"
branch="dev/add-sql-support"

docker run -it \
    -v $test_run_data:/run_data \
    coastsat \
    $startDate \
    $endDate \
    $sitename \
    $epsg \
    $tides \
    $connstring \ 
    $branch