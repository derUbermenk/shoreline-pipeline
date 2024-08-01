test_run_data=/home/admini/Documents/shoreline-pipeline/images/grabtide/test_run_data/tides

startDate="20240601" 
endDate="20240701"
savePath=/tides
station_id=9440083
branch=main

docker run -it \
    -v $test_run_data:/tides \
    grabtide \
    $startDate $endDate $savePath $station_id $branch

