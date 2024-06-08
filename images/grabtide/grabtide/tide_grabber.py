#!/usr/bin/env python

import argparse
import requests
import os
import sys

class TideGrabber():
    def __init__(self, startDate: str, endDate: str, saveDir: str):
        """Initializes a tide grabber object

        Parameters
        ----------
        startDate: str
            yyyymmdd
        endDate: str
            yyyymmdd
        saveDir: str
            yyyymmdd
        """
        self.startDate = startDate
        self.endDate = endDate
        self.saveDir = saveDir.rstrip('/')

        self.savePath = self.formatSavePath()
        return

    def formatSavePath(self):
        return os.path.join(self.saveDir, f"{self.startDate}_{self.endDate}.csv")

    def request(self):
        url = 'https://tidesandcurrents.noaa.gov/api/datagetter' 
        params = {
            'product': 'predictions',
            'application': 'NOS.COOPS.TAC.WL',
            'begin_date': '20240608',
            'end_date': '20240609',
            'datum': 'MSL',
            'station': '1631428',
            'time_zone': 'GMT',
            'units': 'metric',
            'interval': '6',
            'format': 'csv'
        }

        response = requests.get(url, params)

        if response.status_code == 200:
            return response.content
        else:
            print(f'Failed to retrieve data: {response.status_code}')
            sys.exit(1)

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
    if os.path.exists(path) and os.path.isdir(path):
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

    checkDirExists(args_.saveDir)

    tide_grabber = TideGrabber(args_.startdate, args_.enddate, args_.saveDir)
    return tide_grabber