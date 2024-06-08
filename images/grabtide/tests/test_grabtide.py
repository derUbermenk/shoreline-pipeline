from grabtide.tide_grabber import TideGrabber

def test_initializeGrabTide(mocker):
    startDate = 20240101
    endDate = 20240131
    saveDir = "path/to/saveDir/"
    expected_savePath = "{saveDir}{startDate_endDate}.csv"

    args = [startDate, endDate, saveDir]

    tide_grabber =  initializeTideGrabber()
    assert isinstance(tide_grabber, TideGrabber)

    assert formatter.startDate == startDate
    assert formatter.endDate == endDate
    assert formatter.save_path == expected_savePath 

  