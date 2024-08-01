#!/bin/bash

show_help() {
  echo "Usage: $(basename $0) args"
  echo "  -v, --version  Display version information"
  echo "  start date"
  echo "  end date"
  echo "  save path"
  echo "  station id"
  echo "  branch"
  exit 0
}

if [ "$1" = "-h" -o "$1" = "--help" ]; then
  show_help
fi

startDate=$1
endDate=$2
savePath=$3
station_id=$4
branch=$5

link=https://api.github.com/repos/derUbermenk/grabtide/tarball/$branch

mkdir /_runner
mkdir /runner

echo "Downloading from $branch"
echo " using: $link"
python -m wget -o /runner.tar $link 

tar -xf /runner.tar -C /_runner
mv /_runner/*/grabtide/* /runner
cp /runner/tide_grabber.py /runner/tide_grabber
chmod +x /runner/tide_grabber

export PATH="/runner:$PATH"

echo "Running tide grabber"
tide_grabber $startDate $endDate $savePath $station_id 