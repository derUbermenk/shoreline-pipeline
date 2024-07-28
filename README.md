<h1>Shoreline Pipeline</h1>

Grabs images of coastlines in a particular location and outputs tide corrected shoreline intersects
<img src="https://github.com/user-attachments/assets/04f68437-3ae0-42fd-88cb-85fa74b6b7ad" alt="image"/>

<h3><i>Planned Features</i></h3>
<ul>
  <li> Add task for refining shoreline intersect positions.
  <p>See <a href="https://github.com/derUbermenk/undergraduate-thesis#:~:text=Smoothen%20detected%20shoreline%20traces">smoothing shorelines</a> at derUbermenk/undergraduate-thesis </p>
    <img src="https://github.com/user-attachments/assets/10910468-96bc-447b-a4ad-73818aebbf2b"  style="width: 40%; height: 40%;" />
  </li>
  
  <li> Add task for computing shoreline change statistics. See <a href="https://github.com/derUbermenk/undergraduate-thesis#:~:text=CoastCR%20for%20calculating%20shoreline%20change%20statistics">computing statics</a> using <a href="https://github.com/alejandro-gomez/CoastCR">CoastCR</a>
  </li>

  <li>Use git and repo branches to control program versions used within each task image. At present, this is only implemented in the parse_intersects tasks. Having this in the other tasks would remove the need to rebuild task images
    everytime the program being ran within is updated. Instead a compressed version of the input branch is downloaded once a container is executed
  </li>
</ul>

<h3><i>Recently implemented</i></h3>
  <ul>
    <li> <a href="https://github.com/derUbermenk/shoreline-intersect-parser">derUbermenk/shoreline-intersect-parser</a>: Add task for csv to geojson transformation to enable storing in GIS supported DBs; PostGIS for example.
    <p>See <a href="https://github.com/derUbermenk/undergraduate-thesis#:~:text=Transform%20data%20into%20workable%20formats">Transform into workable formats</a> </p>
      <img src="https://github.com/user-attachments/assets/9cd59fe1-a54d-4f5f-a54a-eb49ca588c61" alt="image"  style="width: 40%; height: 40%;" />
    <p>Implementation now uses shapely instead of the originally planned in-qgis transformation. Writing a new implementation was more straightforward than refactoring the sphagetti that was my old code</p>
    </li>
  </ul>

<h3> This project utilizes the following resources </h3>
<ul>
<li><a href="https://tidesandcurrents.noaa.gov/tide_predictions.html">NOAA Tide Predictions</a> for fetching tide levels to be used for tidal correction</li>
<li><a href="https://github.com/kvos/CoastSat">CoastSat</a> for mapping shoreline positions</li>
<li><a href="https://github.com/derUbermenk/undergraduate-thesis">scripts used as part of my team's undergraduate thesis<a> for preparing necessary input data</li>
</ul>


### Citations

<p>
Gómez-Pazo, A., Payo, A., Paz-Delgado, M.V., Delgadillo-Calzadilla, M.A. (2022). Open Digital Shoreline Analysis System: ODSAS v1.0. Journal of Marine Science and Engineering, 10, 26. DOI: https://doi.org/10.3390/jmse10010026
</p>

<p>
Vos K., Splinter K.D., Harley M.D., Simmons J.A., Turner I.L. (2019). CoastSat: a Google Earth Engine-enabled Python toolkit to extract shorelines from publicly available satellite imagery. Environmental Modelling and Software. 122, 104528. https://doi.org/10.1016/j.envsoft.2019.104528 (Open Access)
</p>
