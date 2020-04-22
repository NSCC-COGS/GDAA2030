# Name: Maynard_GetFunctions.py
# Keely Maynard
# Purpose: Pull landsat files from Amazon Cloud and create a map and display

#import functions 
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import urllib.request
import os
import tifffile

#define the function loadScenelist which will load the imagery from Amazon
def loadScenelist(sceneList,sceneTest=None,cloudCoverMax=None):

    #read the scenelist file and put it into a pandas dataframe
    sceneDf = pd.read_csv(sceneList, nrows=sceneTest)

    #make the acquistion date field the daytime object 
    sceneDf.acquisitionDate = pd.to_datetime(sceneDf.acquisitionDate)

    #print some example information for: 
    print(sceneDf.head())
    print(sceneDf['acquisitionDate'])
    print(sceneDf.columns)
    
    #filter the scenes to find the ones with a preset cloud cover
    if cloudCoverMax:
        #filter the dataset to the cloud cover that are less than the max
        cloudFilter = sceneDf['cloudCover'] < cloudCoverMax
        #set the sceneDf to the filtered version of sceneDf
        sceneDf = sceneDf[cloudFilter]

    return sceneDf

#define the function find path row which finds the row of the scene
def findPathRow(sceneDf, lat, lon):
    #calculate the distance from our location to each scene
    sceneDf['lat'] = (sceneDf['min_lat'] + sceneDf['max_lat']) / 2.0
    sceneDf['lon'] = (sceneDf['min_lon'] + sceneDf['max_lon']) / 2.0
    sceneDf['dist'] = np.sqrt(( sceneDf['lat'] - lat)**2 + (sceneDf['lon'] - lon)**2)

    #Identifies the nearest path and row
    nearestFilter = sceneDf['dist'].idxmin()
    nearestPath = sceneDf['path'][nearestFilter]
    nearestRow = sceneDf['row'][nearestFilter]

    return nearestPath, nearestRow

#define the function selectScene which selects the scene from the filtered path and rows
def selectScene(sceneDf, path, row):
    #limit the available scenes to the nearest path and row
    sceneDf_nearest = sceneDf[(sceneDf['path']==path) & (sceneDf['row']==row)]

    #find the most recent image from this path and row
    nearestFilter = sceneDf_nearest['acquisitionDate'].idxmax()

    #show the final selected scene
    selectedScene = sceneDf_nearest.loc[nearestFilter]

    return selectedScene

#define getImageIO which retrieves the image from the internet and creates and image
def getImageIO(selectedScene, band, imageDir):
    #find the url for the image
    indexUrl = selectedScene['download_url']
    productId = selectedScene['productId']

    #remove the html
    url = os.path.split(indexUrl)[0]
    #make an image with the band in the name
    imageName = productId + ('_B%i.TIF') % band 

    imageUrl = r'/'.join([url,imageName])
    imagePath = os.path.join(imageDir,imageName)

    print(imageUrl)
    print(imagePath)

    return imageUrl,imagePath

#define downloadImage which downloads the image from the server
def downloadImage(imageUrl,imagePath):
    if not os.path.exists(imagePath):
        print('downloading....', imageUrl)
        response = urllib.request.urlopen(imageUrl)
        imageFile = response.read()
        imageDir = os.path.split(imagePath)[0]
        if not os.path.exists(imageDir):os.makedirs(imageDir)
        with open(imagePath, 'wb') as f:
            f.write(imageFile)
    
    #if the image has already been downloaded
    else:
        print(imagePath, ' already found')

# define plotResults which creates a window which will display the chosen image
def plotResults(lat,lon, selectedScene,sceneDf,imagePath):
    #create the plot
    plt.figure()

    #split the plotting area in two
    plt.subplot(211)

    #limit the total captures included to speed up process
    try:
        plotDf = sceneDf[0:10000]
    except:
        plotDf = sceneDf
    
    #plot the selected images 
    # plt.scatter(plotDf['lon'],plotDf['lat'], c = 'blue', linewidth = 0, marker = '.', alpha = .1)
    plt.scatter(plotDf['lon'], plotDf['lat'], c = plotDf['acquisitionDate'].astype(np.int64), cmap = 'viridis', marker ='.', alpha = .5)

    #plot the selected capture location
    plt.scatter(selectedScene['lon'],selectedScene['lat'], linewidth = 5, marker = 'o', c = 'red')

    #plot the input lat/lon
    plt.scatter(lon,lat, marker = 'x', c='black')

    # some other plots which you can do:
    # plt.scatter(plotDf.mean_lon, plotDf.mean_lat,c=plotDf.acquisitionDate.astype(np.int64), cmap = 'viridis', marker ='.', alpha = .5)
    # plt.scatter(sceneDf_nearest.mean_lon,sceneDf_nearest.mean_lat, linewidth = 5, marker = 'o', c = 'red')

    #set the image as the tiff image
    image = tifffile.imread(imagePath)

    print(image.shape)
    
    #display the image in the second part of the plotted area
    plt.subplot(212)
    imagePreview = image[::10,::10]
    plt.imshow(imagePreview, cmap = 'bone')

    # display the plot
    plt.show()