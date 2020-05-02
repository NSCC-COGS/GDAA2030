#==================================
# Image Analytics
# Acquiring an Image GDAA2030
# Purpose: acquire an image. call functions from getLandsat_functions.py
# A.Drake  Feb 11 2020
#=================================

import getLandsat_functions as glf

# info located at https://docs.opendata.aws/landsat-pds/readme.html
# for this code we will allow an input coordinate
#  and search for the closests, nearest landsat 8 scene
#  for a given band based on a scene list
#  we will also filter by cloud cover percentage

lat = 59.09
lon = -109.259
band = 1
cloudCoverMax = 2
sceneList = "scene_list.txt"
sceneTest = 20 # set a small number to test, or None
imageDir = r'.\images'


sceneDf = glf.loadSceneList(sceneList, sceneTest, cloudCoverMax)
sceneDf = glf.loadSceneList(sceneList)

path,row = glf.findPathRow(sceneDf, lat, lon)

print(path, row)

selectedScene = glf.selectScene(sceneDf, path, row)

print(selectedScene)

imageUrl, imagePath = glf.getImageIO(selectedScene, band, imageDir)
glf.downloadImage(imageUrl, imagePath)

glf.plotResults(lat,lon, selectedScene, sceneDf, imagePath)