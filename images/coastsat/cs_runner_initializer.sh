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
savePath=$3
coordinates=$4
sitename=$5
epsg=$6
transects=$7
tides=$8
ref_shoreline=$9

# runner variables
reponame="CoastSat"
branch=${10}

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

cs_runner $startDate $endDate $savePath $coordinates $sitename \
    $epsg $transects $tides $ref_shoreline
