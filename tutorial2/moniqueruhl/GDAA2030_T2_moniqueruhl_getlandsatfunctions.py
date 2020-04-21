'''
Script Name  : GDAA2030_T2_moniqueruhl_getlandsatfunctions.py
Purpose      : Create functions needed to access landsat 8 scenes listed in scene_list 
Written By   : M Ruhl, 2020.02.11
'''
import pandas as pd #python package for working with structured data, like R's data.frame
import numpy as np 
from matplotlib import pyplot as plt 
import urllib.request
import os
import tifffile

#create function to load scene list file using pandas
def loadSceneList(sceneList, sceneTest=None, cloudCoverMax=None):
    #read the scene list into a dataframe object
    sceneDf=pd.read_csv(sceneList,nrows=sceneTest)

    #set aquisition data field as datetime object
    sceneDf.acquisitionDate=pd.to_datetime(sceneDf.acquisitionDate) #read_csv is reading the aquisition date as a string, want to set to datatime object instead

    #print some example information for
    print(sceneDf.head()) #showing all headers within sceneDf
    #function for showing how pandas is reading the columns (i.e. what data types?)?
    print(sceneDf['acquisitionDate'])
    print(sceneDf.columns)

    if cloudCoverMax:
        #filters the dataset to specified cloud percentage
        cloudFilter=sceneDf['cloudCover']<cloudCoverMax
        sceneDf=sceneDf[cloudFilter]
    return sceneDf

#create function for finding nearest path and row of specified lat long
def findPathRow(sceneDf,lat,lon):
    #calculate the distance from our lat/long to each scene, most recent scene by searching path row, not nearest
    sceneDf['lat']=(sceneDf['min_lat'] + sceneDf['max_lat'])/2.0 #using euclidean distances even though coordinates still in lat/long (should convert to itf)
    sceneDf['lon']=(sceneDf['min_lon'] + sceneDf['max_lon'])/2.0
    sceneDf['dist']=np.sqrt((sceneDf['lat']-lat)**2 + (sceneDf['lon']-lon)**2)

    #find nearest path/row
    nearestFilter=sceneDf['dist'].idxmin()
    nearestPath=sceneDf['path'][nearestFilter]
    nearestRow=sceneDf['row'][nearestFilter]

    return nearestPath,nearestRow

#create function to select the newest scene from the nearest path and row
def selectScene(sceneDf,path,row):
    sceneDf_nearest=sceneDf[(sceneDf['path']==path) & (sceneDf['row']==row)]

    #find nearest capture in the nearest path and row
    newestFilter=sceneDf_nearest['acquisitionDate'].idxmax()

    #report the final selected scene
    selectedScene=sceneDf_nearest.loc[newestFilter]

    return selectedScene

def getImageID(selectedScene,band,imageDir):
    #repot the URL for the image index
    indexUrl=selectedScene['download_url']
    productId=selectedScene['productId']

    url=os.path.split(indexUrl)[0] #drops the html index
    imageName=productId + ('_B%i.TIF') % band

    imageUrl=r'/'.join([url,imageName]) #standard split format
    imagePath=os.path.join(imageDir,imageName) #joins image name and url

    print (imageUrl)
    print (imagePath)

    return imageUrl,imagePath

def downloadImage(imageUrl,imagePath):
    
    if not os.path.exists(imagePath):
        print ('downloading...', imageUrl)
        response=urllib.request.urlopen(imageUrl)
        imageFile=response.read()
        imageDir=os.path.split(imagePath)[0]
        if not os.path.exists(imageDir):os.makedirs(imageDir)
        with open(imagePath,'wb') as f:
            f.write(imageFile)
    else:
        print(imagePath,'already found')


#create function to plot results
def plotResults(lat,lon, selectedScene,sceneDf,imagePath):
    #prepare a plot
    plt.figure()

    #assign plotting area to 2x1 subplot, starting with area 1
    plt.subplot(211)

    #reduce the total captures to a maximum to speed up  plotting 
    try:
        plotDf = sceneDf[0:10000]
    except:
        plotDf = sceneDf

    #plot the reduced set of all image captures
    # plt.scatter(plotDf['lon'],plotDf['lat'], c='blue', linewidth = 0, marker ='.', alpha = .1)
    plt.scatter(plotDf['lon'],plotDf['lat'],c=plotDf['acquisitionDate'].astype(np.int64), cmap = 'viridis', marker ='.', alpha = .5)

    #plot the selected capture location
    plt.scatter(selectedScene['lon'],selectedScene['lat'], linewidth =5, marker = 'o', c='red')

    #plot the input lat/lon
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
