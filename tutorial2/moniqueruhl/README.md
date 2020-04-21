# Tutorial 2 - Acquiring Images

### Sourcing geospatial images from freely available data.

Scraping Landsat data from the gz file listed here:
>[Landsat on Amazon Web Services](https://docs.opendata.aws/landsat-pds/readme.html)

GDAA2030_T2_moniqueruhl_getlandsat will utilize fucntions created in GDAA2030_T2_moniqueruhl_getlandsatfunctions. The purpose of the script is to download a Landsat 8 scene based on the user specified lat and long coordinates, band number, and maximum allowable cloud cover. The output will include an image of the scene and a world map with the location of the scene plotted and the number of all available scenes symbolized.
