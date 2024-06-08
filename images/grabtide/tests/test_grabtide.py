from grabtide.tide_grabber import TideGrabber

def test_initializeTideGrabber(mocker):
    startDate = 20240101
    endDate = 20240131
    saveDir = "path/to/saveDir/"
    expected_savePath = "{saveDir}{startDate_endDate}.csv"

    args = [startDate, endDate, saveDir]

    # mock checkPath
    mocker.patch('grabtide.tide_grabber.checkPath')

    tide_grabber =  initializeTideGrabber(args)
    assert isinstance(tide_grabber, TideGrabber)

    assert tide_grabber.startDate == startDate
    assert tide_grabber.endDate == endDate
    assert tide_grabber.save_path == expected_savePath 