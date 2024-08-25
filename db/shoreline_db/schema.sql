CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE Shorelines (
    sitename VARCHAR(20) PRIMARY KEY,
    loc VARCHAR(50),
    NSM DOUBLE PRECISION,
    SCE DOUBLE PRECISION,
    LRR DOUBLE PRECISION,
    WLR DOUBLE PRECISION,
    -- crs to use for calculating detected shoreline positions
    --  also used as crs for baseline
    output_epsg VARCHAR(50) NOT NULL DEFAULT 'EPSG:4326',
    -- used as reference for determining shoreline. must use
    --  output crs
    baseline geometry(LINESTRING) NOT NULL,
    -- uses EPSG:4326
    area  geometry(POLYGON) NOT NULL
);

CREATE TABLE Profiles (
    record_date DATE PRIMARY KEY,
    shoreline_sitename VARCHAR(20) NOT NULL REFERENCES Shorelines(sitename) ON DELETE CASCADE,
    satname VARCHAR(5),
    geoaccuracy VARCHAR(10),
    cloud_cover DOUBLE PRECISION,
    geom geometry(MULTILINESTRING)
); 

CREATE TABLE Transects (
    id SERIAL PRIMARY KEY,
    transect_name VARCHAR(5) NOT NULL,
    shoreline_sitename VARCHAR(20) NOT NULL REFERENCES Shorelines(sitename) ON DELETE CASCADE,
    geom geometry(LINESTRING),
    CONSTRAINT unique_transect_shoreline UNIQUE(transect_name, shoreline_sitename)
);

CREATE TABLE Intersects (
    id INT,
    profile_record_date DATE NOT NULL REFERENCES Profiles(record_date) ON DELETE CASCADE,
    transect_id INT NOT NULL REFERENCES Transects(id) ON DELETE CASCADE,
    distance DOUBLE PRECISION NOT NULL,
    geom geometry(POINT),

    CONSTRAINT unique_id_transect_shoreline UNIQUE(id, profile_record_date, transect_id)
);