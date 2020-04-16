#info at https://docs.opendata.aws/landsat-pds/readme.html

#lets import some libraries!
#if they dont exist try (in command prompt)
'''
    py -3.8 -m pip install LIBRARY' 
'''

import getLandsat_functions as glf

''' for this code we will allow an input coordinate
and search for the closest, nearest landsat 8 scene 
for a given band based on a scene list
we will also filter by cloud cover percentage'''

lat = 44.88
lon = -65.16
band = 1
cloudCoverMax = 2
sceneList = "scene_list.txt"
# sceneList = r"C:\_cloud\OneDrive - Nova Scotia Community College\GDAA2030\Tutorial - 1\Tutorial2_working\scene_list.txt"
sceneTest = None # set a small number to test, or None
imageDir = r'.\images'

sceneDf = glf.loadSceneList(sceneList, sceneTest, cloudCoverMax)
# sceneDf = glf.loadSceneList(sceneList)

path,row = glf.findPathRow(sceneDf, lat, lon)

# print(path, row)

selectedScene = glf.selectScene(sceneDf, path, row)

print(selectedScene)

imageUrl, imagePath = glf.getImageIO(selectedScene, band, imageDir)

glf.downloadImage(imageUrl,imagePath)

glf.plotResults(lat,lon, selectedScene,sceneDf,imagePath)
