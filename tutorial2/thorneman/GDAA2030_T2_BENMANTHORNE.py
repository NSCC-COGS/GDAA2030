import getLandsat_functions as glf 

## this code will allow an input coordinate 
## then search for the nearest landsat 8 scene 
## for a given band based on a scene list 
## we will also filter by cloud cover % 

lat = 46.22 
lon = -64.55 
band = 1 
cloudCoverMax = 2 
sceneList = "scene_list.txt"
sceneTest = 20 # small number or none for test 
imageDir = r'.\images'

scene = glf.loadSceneList(sceneList, sceneTest, cloudCoverMax)
sceneDf = glf.loadSceneList(sceneList)

path,row = glf.findPathRow(sceneDf, lat, lon)

# print(path,row) 

selectedScene = glf.selectScene(sceneDf, path, row)

print(selectedScene)

imageUrl, imagePath = glf.getImageIO(selectedScene, band, imageDir)

# calls the downloadImage function to collect the image from its online source
glf.downloadImage(imageUrl,imagePath)

# calls the plotResults function to show the image and where it was pulled from
glf.plotResults(lat,lon,selectedScene,sceneDf,imagePath)