'''
Script Name  : GDAA2030_T2_moniqueruhl_getlandsat.py
Purpose      : Getting landsat scenes from specifing a lat/long location and it chooses the appropriate path 
               row number for landsat 8 scene for a specified band. Also specify the cloud cover percetnage 
               threshold.
Written By   : M Ruhl, 2020.02.11
'''
import GDAA2030_T2_moniqueruhl_getlandsatfunctions as glf

lat=68.504135
lon=-115.564856
band=3
cloudCoverMax=2
sceneList="scene_list.txt"
sceneTest=None #set a small number to test, or set to None
imageDir=r'.\images' 

sceneDf=glf.loadSceneList(sceneList,sceneTest,cloudCoverMax)

path,row=glf.findPathRow(sceneDf,lat,lon)

print (path,row)

selectedScene=glf.selectScene(sceneDf,path,row)

print(selectedScene)

imageUrl,imagePath=glf.getImageID(selectedScene,band,imageDir)

glf.downloadImage(imageUrl,imagePath)

glf.plotResults(lat,lon, selectedScene,sceneDf,imagePath)
