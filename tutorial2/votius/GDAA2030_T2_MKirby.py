########################################################################
# ASSIGNMENT : Tutorial 2                                              #
# NAME       : M Kirby                                              #
# DATE       : Feb 25 2020                                             #
########################################################################

import GDAA2030_T2_functions_MKirby as glf

# change lat and long to your location
# this current location is Wuhan, China
lat = 30.59
lon = 114.28
band = 4   # selected band
cloudCoverMax = 2
sceneList = 'scene_list.txt'
sceneTest = None # low number or None for testing
imageDir = r'.\images'

# Loads the SceneList text file
sceneDf = glf.loadSceneList(sceneList,sceneTest,cloudCoverMax)

# Gets the path and row, prints results
path,row = glf.findPathRow(sceneDf,lat,lon)
print(path, row)

# Selects the scene with the best fit to parameters
selectedScene = glf.selectScene(sceneDf,path,row)
print(selectedScene)

# Generates the image url and path
imageUrl, imagePath = glf.getImageIO(selectedScene, band, imageDir)

# Downloads the image
glf.downloadImage(imageUrl, imagePath)

# Plots the results in matplotlib, showing a map of scenes, and your own scene
# also plots an image of your selected band

glf.plotResults(lat,lon, selectedScene, sceneDf, imagePath)