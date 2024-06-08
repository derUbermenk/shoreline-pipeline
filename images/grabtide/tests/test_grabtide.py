from grabtide import TideGrabber, checkDirExists, initializeTideGrabber
import tempfile
from unittest.mock import Mock, patch
from requests import Response

def test_checkDirExists(mocker):    
    """
        Test grabtide.checkDirExists 

        pass conditions:
            function exits with code 1 on non existent path 
            does not exit when given directory exists 
    """
    temp_path = tempfile.TemporaryDirectory()
    nonExistentFilePath = "/non/existent/path/"
    existentFilePath = temp_path.name

    # it exits with code 1 if path does not exist
    try:
        checkDirExists(nonExistentFilePath)
    except SystemExit as e:
        assert True 
        assert e.code == 1
    else:
        assert False 

    # it does not exit if path exist
    try:
        checkDirExists(existentFilePath)
    except SystemExit as e:
        assert False
    else:
        assert True


def test_initializeTideGrabber(mocker):
    """test initializeTideGrabber"""
    startDate = "20240101"
    endDate = "20240131"
    saveDir = "path/to/saveDir/"
    expected_savePath = f"{saveDir}{startDate}_{endDate}.csv"

    args = [startDate, endDate, saveDir]

    # mock checkPath
    mocker.patch('grabtide.tide_grabber.checkDirExists')

    tide_grabber =  initializeTideGrabber(args)
    assert isinstance(tide_grabber, TideGrabber)

    assert tide_grabber.startDate == startDate
    assert tide_grabber.endDate == endDate
    assert tide_grabber.savePath == expected_savePath 

    # set 2: even when save dir is lacking a trailing /
    startDate = "20240101"
    endDate = "20240131"
    saveDir = "path/to/saveDir"
    expected_savePath = f"{saveDir}/{startDate}_{endDate}.csv"

    args = [startDate, endDate, saveDir]

    tide_grabber =  initializeTideGrabber(args)
    assert isinstance(tide_grabber, TideGrabber)

    assert tide_grabber.startDate == startDate
    assert tide_grabber.endDate == endDate
    assert tide_grabber.savePath == expected_savePath

def test_TideGrabber_request_sucess():
    """Test the behaviour of of TideGrabber.request on success

    expect function to call request with the correct params 
    expect function to return a response object if status code  == 200 
    expect function to return with sys exit 1 if status code is not == 200
    """
    startDate = "20240101"
    endDate = "20240131"
    saveDir = "path/to/saveDir"

    correct_url = 'https://tidesandcurrents.noaa.gov/api/datagetter' 
    correct_params = {
        'product': 'predictions',
        'application': 'NOS.COOPS.TAC.WL',
        'begin_date': startDate,
        'end_date': endDate,
        'datum': 'MSL',
        'station': '1631428',
        'time_zone': 'GMT',
        'units': 'metric',
        'interval': '6',
        'format': 'csv'
    }

    tide_grabber = TideGrabber(startDate, endDate, saveDir)

    successful_response = Mock() 
    successful_response.status_code = 200 
    successful_response.content = b'sucess'
    with patch("requests.get", return_value=successful_response) as mock_get:

        try:
            response_content = tide_grabber.request()
        except SystemExit as e:
            assert False, "sucessful request exited, when expected not to"
        else:
            assert True

        mock_get.assert_called_once_with(correct_url, correct_params)
        assert isinstance(response_content, bytes)


def test_TideGrabber_request_unsucessful():
    """Test the behaviour of of TideGrabber.request on fail 

    expect function to call request with the correct params 
    expect function to return a response object if status code  == 200 
    expect function to return with sys exit 1 if status code is not == 200
    """
    startDate = "20240101"
    endDate = "20240131"
    saveDir = "path/to/saveDir"

    correct_url = 'https://tidesandcurrents.noaa.gov/api/datagetter' 
    correct_params = {
        'product': 'predictions',
        'application': 'NOS.COOPS.TAC.WL',
        'begin_date': startDate,
        'end_date': endDate,
        'datum': 'MSL',
        'station': '1631428',
        'time_zone': 'GMT',
        'units': 'metric',
        'interval': '6',
        'format': 'csv'
    }


    tide_grabber = TideGrabber(startDate, endDate, saveDir)

    unsuccessful_response = Mock() 
    unsuccessful_response.status_code = 404

    mock_get = patch("requests.get", return_value=unsuccessful_response).start()
    mock_print = patch("builtins.print").start()
 

    response_content = None
    try:
        response_content = tide_grabber.request()
    except SystemExit as e:
        assert True 
        assert e.code == 1
    else:
        assert False, "unsuccessful request did not exit when expected to have"

    mock_get.assert_called_once_with(correct_url, correct_params)
    mock_print.assert_called_once_with(f'Failed to retrieve data: 404')
    assert response_content == None

def test_TideGrabber_run():
    """Test behaviour of TideGrabber.run()

    expect function to save the content of response to correct file path
    """

    pass