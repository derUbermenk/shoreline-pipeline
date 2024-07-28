# intersect=2024-06-01_2024-07-01_data.csv
intersect=2024-05-01_2024-06-01_data.csv
intersect_date=$(basename -s .csv $intersect) 
workdir=/home/admini/Documents/shoreline-pipeline/images/shoreline-intersect-parser/test_run
echo $intersect_date

docker run -it \
    -v ${workdir}/input:/input \
    -v ${workdir}/output:/output \
    shoreline-intersect-parser \
    /input/transects.geojson \
    /input/$intersect \
    /output/${intersect_date}_segments.geojson \
    dev/create-parser



