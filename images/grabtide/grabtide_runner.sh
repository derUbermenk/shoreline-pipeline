#!/bin/bash

show_help() {
  echo "Usage: $(basename $0) args"
  echo "  -v, --version  Display version information"
  echo "  start date"
  echo "  end date"
  echo "  save path"
  echo "  station id"
  exit 0
}

if [ "$1" = "-h" -o "$1" = "--help" ]; then
  show_help
fi

startDate=$1
endDate=$2
savePath=$3
station_id=$4
bucketName=$5
s3Key=$6

shift 6

# Check if the required parameters are provided
if [[ -z "$startDate" || -z "$endDate" || -z "$savePath" || -z "$station_id" || -z "$bucketName" || -z "$s3Key" ]]; then
    echo "Error: Missing required parameters!"
    exit 1
fi

link=https://api.github.com/repos/derUbermenk/grabtide/tarball/$BRANCH

mkdir /_runner
mkdir /runner

# Loop through remaining arguments to parse optional parameters
while [[ $# -gt 0 ]]; do
    case "$1" in
        --units)
            units="$2"
            shift 2
            ;;
        --interval)
            interval="$2"
            shift 2
            ;;
        --timezone)
            timzeone="$2"
            shift 2
            ;;
        --datum)
            datum="$2"
            shift 2
            ;;
        --useAccessKeys)
            useAccessKeys="true"
            shift
            ;;
        # Catch-all for unknown flags
        --*) 
            echo "Unknown option: $1"
            shift
            ;;
        *)
            echo "Unexpected argument: $1"
            shift
            ;;
    esac
done

echo "Downloading from $BRANCH"
echo " using: $link"
python -m wget -o /runner.tar $link 

tar -xf /runner.tar -C /_runner
mv /_runner/*/grabtide/* /runner
cp /runner/tide_grabber.py /runner/tide_grabber
chmod +x /runner/tide_grabber

export PATH="/runner:$PATH"

echo "Running tide grabber with the following arguments"
echo "startDate $startDate"
echo "endDate $endDate"
echo "savePath $savePath"
echo "station_id $station_id"
echo "useAccessKeys $useAccessKeys"

tide_grabber $startDate $endDate $savePath $station_id $bucketName $s3Key\
 ${units:+--units "$units"}\
 ${interval:+--interval "$interval"}\
 ${timezone:+--timezone "$timezone"}\
 ${datum:+--datum "$datum"}\
 ${useAccessKeys:+--useAccessKeys}