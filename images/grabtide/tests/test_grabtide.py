from grabtide import TideGrabber, checkDirExists, initializeTideGrabber
import tempfile

def test_checkDirExists(mocker):    
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