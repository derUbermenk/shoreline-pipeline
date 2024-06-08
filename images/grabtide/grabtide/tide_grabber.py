#!/usr/bin/env python

import argparse
import requests
import os
import sys

class TideGrabber():
    def __init__(self):
        return

    def run(self):    
        return

def checkDirExists(path: str):
    """Checks if save directory exists 

    checks if the dir in the given path exists. exists the program if it doesnt

    Paremeters:
    ----------
    path: str
        path to directory 
    """
    if os.path.exists(path):
        return
    else:
        sys.exit(1)
    
def initializeTideGrabber(args) -> TideGrabber:
    parser = argparse.ArgumentParser(
        prog="TideGrabber",
        description="downloads a csv file of MSL tide data from NOAA websites"
    )

    parser.add_argument('startdate', help='start date of range (yyyymmdd)')
    parser.add_argument('enddate', help='end date of range (yyyymmdd)')
    parser.add_argument('saveDir', help='save dir of csv file')
    parser.add_argument('--stationid', help='stationid')
    parser.add_argument('--units', help='units')
    parser.add_argument('--interval', help='interval')
    parser.add_argument('--timezone', help='timezone')
    parser.add_argument('--datum', help='datum')

    args_ = parser.parse_args(args)

    checkDirExists(args.saveDir)

    tide_grabber = TideGrabber(args.startdate, args.enddate, args.saveDir)
    return tide_grabber