########################################################################
# ASSIGNMENT : Tutorial 2                                              #
# NAME       : M Kirby                                              #
# DATE       : Feb 25 2020                                             #
########################################################################
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import urllib.request
import os
import tifffile

def loadSceneList(sceneList,sceneTest=None,cloudCoverMax=None):

    # read the scenelist file into a pandas dataframe
    sceneDf = pd.read_csv(sceneList, nrows=sceneTest)

    # set the acquisition date field as the datetime object
    sceneDf.acquisitionDate = pd.to_datetime(sceneDf.acquisitionDate)

    # print some example information for:
    print(sceneDf.head())
    print(sceneDf['acquisitionDate'])
    print(sceneDf.columns)

    if cloudCoverMax:
        # lers filter the dataset down to just clouds less than a....
        cloudFilter = sceneDf['cloudCover'] < cloudCoverMax
        # sets sceneDf to the filtered version of sceneDf
        sceneDf = sceneDf[cloudFilter]

    return sceneDf

def findPathRow(sceneDf, lat, lon):
    # calculate the distance from our location to each scene
    sceneDf['lat'] = (sceneDf['min_lat'] + sceneDf['max_lat']) / 2.0
    sceneDf['lon'] = (sceneDf['min_lon'] + sceneDf['max_lon']) / 2.0
    sceneDf['dist'] = np.sqrt(( sceneDf['lat'] - lat)**2 + (sceneDf['lon'] - lon)**2)

    # now lets find the nearest path/row
    nearestFilter = sceneDf['dist'].idxmin()
    nearestPath = sceneDf['path'][nearestFilter]
    nearestRow = sceneDf['row'][nearestFilter]

    return nearestPath, nearestRow

def selectScene(sceneDf, path, row):
    #reduce rhe available scenes down to nearest path/row
    sceneDf_nearest = sceneDf[(sceneDf['path']==path) & (sceneDf['row']==row)]

    # now find the newest capture in the nearest path/row
    nearestFilter = sceneDf_nearest['acquisitionDate'].idxmax()

    # report the final selected scene
    selectedScene = sceneDf_nearest.loc[nearestFilter]

    return selectedScene

def getImageIO(selectedScene, band, imageDir):
    # report the URL for the image index
    indexUrl = selectedScene['download_url']
    productId = selectedScene['productId']

    # strips off the .html
    url = os.path.split(indexUrl)[0]
    # creates a image name with our band
    imageName = productId + ('_B%i.TIF') % band

    imageUrl = r'/'.join([url,imageName])
    imagePath = os.path.join(imageDir,imageName)

    print(imageUrl)
    print(imagePath)

    return imageUrl,imagePath

def downloadImage(imageUrl,imagePath):
    if not os.path.exists(imagePath):
        print('downloading....', imageUrl)
        response = urllib.request.urlopen(imageUrl)
        imageFile = response.read()
        imageDir = os.path.split(imagePath)[0]
        if not os.path.exists(imageDir):os.makedirs(imageDir)
        with open(imagePath, 'wb') as f:
            f.write(imageFile)

    else:
        print(imagePath, ' already found')

def plotResults(lat,lon, selectedScene,sceneDf,imagePath):
    #prepare a plot

    plt.figure(num='Mark Kirby - Tutorial 2')

    # assign plotting area to 2x1 subplot, starting with area 1
    plt.subplot(211)

    #reduce the total captures to a maximum to speed up  plotting
    try:
        plotDf = sceneDf[0:10000]
    except:
        plotDf = sceneDf

    #plot the reduced set of all image captures
    # plt.scatter(plotDf['lon'],plotDf['lat'], c='blue', linewidth = 0, marker ='.', alpha = .1)
    plt.scatter(plotDf['lon'],plotDf['lat'],c=plotDf['acquisitionDate'].astype(np.int64), cmap = 'viridis', marker ='.', alpha = .5)

    # plot the selected capture location
    plt.scatter(selectedScene['lon'],selectedScene['lat'], linewidth =5, marker = 'o', c='red')

    # plot the input lat/lon
    plt.scatter(lon,lat, marker = 'x', c='black')

    ''' some other plots include:
    # plt.scatter(plotDf.mean_lon,plotDf.mean_lat,c=plotDf.acquisitionDate.astype(np.int64), cmap = 'viridis', marker ='.', alpha = .5)
    # plt.scatter(sceneDf_nearest.mean_lon,sceneDf_nearest.mean_lat, linewidth =5, marker = 'o', c='red')
    '''

    image = tifffile.imread(imagePath)

    print(image.shape)

    plt.subplot(212)
    imagePreview = image[::10,::10]
    plt.imshow(imagePreview, cmap='bone')

    plt.show()

