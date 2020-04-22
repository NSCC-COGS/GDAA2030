#Name: Maynard_GetLandsat.py
#Purpose: Specify and call the landsat image of a determined area and display it as a plot

#import the Maynard_GetFunctions to run the functions to isolate the imagery
import Maynard_GetFunctions as glf

#Set the settings for the satellite imagery 
lat = 20.239570
lon = 105.724550      #location of the endangered primate research centre in Vietnam
band = 4
cloudCoverMax = 2
sceneList = 'scene_list.txt'
sceneTest = None        # low number or none is best for testing
imageDir = r'.\images'

#call the function loadSceneList to define the list of scenes based on teh settings set above
sceneDf = glf.loadScenelist(sceneList,sceneTest,cloudCoverMax)

#call function findPathRow to determine the closest path and row to the lat/lon
path,row = glf.findPathRow(sceneDf,lat,lon)
print(path, row)

#call the selectScene function to select the scene from the previous results 
selectedScene = glf.selectScene(sceneDf,path,row)
print(selectedScene)

#define the image url and image path based on the getImageIO function 
imageUrl, imagePath = glf.getImageIO(selectedScene, band, imageDir)

#download the selected image from Amazon cloud
glf.downloadImage(imageUrl, imagePath)

# display the results using the settings set in plotResults function
glf.plotResults(lat,lon, selectedScene, sceneDf, imagePath)

