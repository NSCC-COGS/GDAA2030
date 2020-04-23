################################
# GDAA2030_T2_JordanKempff.py
# Jordan Kempff
# February 25, 2020
################################

import GDAA2030_T2_functions_JordanKempff as glf 
''' for this code wer will allow an input coordinate and search for the closest, nearest landsat 8 
scene for a given band based on a scene list
we will also filter by cloud cover percentage.'''

# specify the scene location and variables
lat = 43.33
lon = -79.80
band = 1
cloudCoverMax = 2
sceneList = "scene_list.txt"
sceneTest = None
imageDir = r'.\images'

# load the list of scenes
sceneDf = glf.loadSceneList(sceneList, sceneTest, cloudCoverMax)

path,row = glf.findPathRow(sceneDf, lat, lon)

# show the selected scene number
selectedScene = glf.selectScene(sceneDf, path, row)
print(selectedScene)

imageUrl, imagePath = glf.getImageIO(selectedScene, band, imageDir)

# download the selected scene
glf.downloadImage(imageUrl, imagePath)

# Plot the results of the scene as well as the location of all scenes
glf.plotResults(lat,lon, selectedScene,sceneDf,imagePath)