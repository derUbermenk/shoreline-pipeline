#!/bin/bash

show_help() {
  echo "Usage: $(basename $0) args"
  echo "  -v, --version  Display version information"
  echo "  path to transects geojson"
  echo "  path to intersects csv"
  echo "  save path for segments geojson"
  echo "  branch to use"
  exit 0
}

if [ "$1" = "-h" -o "$1" = "--help" ]; then
  show_help
fi

transect=$1
intersects=$2
segments=$3
branch=$4

link=https://api.github.com/repos/derUbermenk/shoreline-intersect-parser/tarball/$branch

mkdir /_parser
mkdir /parser

echo "Downloading from $branch"
echo " using: $link"
python -m wget -o /parser.tar $link 

tar -xf /parser.tar -C /_parser
mv /_parser/*/* /parser
cp /parser/intersect_parser.py /parser/intersect_parser
chmod +x /parser/intersect_parser

export PATH="/parser:$PATH"
echo $PATH
ls /parser
intersect_parser $1 $2 $3