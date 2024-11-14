test_run_data=/home/admini/Documents/shoreline-pipeline/images/grabtide/test_run_data/tides

startDate="20240601" 
endDate="20240701"
savePath=/tides
station_id=9440083
branch='dev/update-process-to-save-to-s3'
bucketName='shoreline-bucket-randomadobe'
s3Key='tides/test_run.csv'
useAccessKeys='--useAccessKeys'

docker run -it \
    -v $test_run_data:/tides \
    -e BRANCH=$branch\
    -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID\
    -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY\
    grabtide $startDate $endDate $savePath $station_id $bucketName $s3Key $useAccessKeys

