from CoastSat import initializeCoastSatRunner, CoastSatRunner

def test_initializeCoastSatRunner():


    startDate = "2024-01-01"
    endDate = "2024-02-01"
    saveDir = "/data"
    coordinates = "[ \
        [144.79485033965136, 13.429388175797682], \
        [144.80045079197197, 13.428688997897156], \
        [144.78536604893787, 13.42058047237599],  \
        [144.78098868383339, 13.421999744999741]  \
    ]"
    sitename = "PAGO",
    epsg = "6637"
    transects = "/data/transects.geojson"
    tides = "/data/tides.csv"
    path_to_ref_shoreline = "/data/path_to_ref_shoreline.csv"

    args = [
        startDate,
        endDate,
        saveDir,
        coordinates,
        sitename,
        epsg,
        transects,
        tides,
        path_to_ref_shoreline
    ]

    coastSatRunner = initializeCoastSatRunner(args)

    assert isinstance(coastSatRunner, CoastSatRunner)
    assert coastSatRunner.startDate == startDate   
    assert coastSatRunner.endDate == endDate
    assert coastSatRunner.saveDir == saveDir
    assert coastSatRunner.coordinates == [
        [144.79485033965136, 13.429388175797682],
        [144.80045079197197, 13.428688997897156],
        [144.78536604893787, 13.42058047237599],
        [144.78098868383339, 13.421999744999741] 
    ]
    assert coastSatRunner.sitename == sitename
    assert coastSatRunner.epsg == epsg
    assert coastSatRunner.path_to_transects == transects
    assert coastSatRunner.path_to_tides == tides
