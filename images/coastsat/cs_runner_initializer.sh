show_help() {
  echo "Usage: $(basename $0) args"
    echo "  startDate"
    echo "  endDate"
    echo "  savePath"
    echo "  coordinates"
    echo "  sitename"
    echo "  epsg"
    echo "  transects"
    echo "  tides"
    echo "  ref_shoreline"
    exit 0
}

# coastsat specific variables
startDate=$1
endDate=$2
sitename=$3
epsg=$4
tides=$5
connstring=$6

# runner variables
reponame="CoastSat"
branch=$7

link=https://api.github.com/repos/derUbermenk/$reponame/tarball/$branch
echo $link

curl -Lo /runner.tar $link 

mkdir /_runner
mkdir /runner

tar -xf /runner.tar -C /_runner
ls /runner
mv /_runner/*/CoastSat/* /runner
cp /runner/coastSatRunner_DB.py /runner/cs_runner
chmod +x /runner/cs_runner

export PATH="/runner:$PATH"

cs_runner $startDate \
  $endDate \
  $sitename \
  $epsg \
  $tides \
  $connstring

