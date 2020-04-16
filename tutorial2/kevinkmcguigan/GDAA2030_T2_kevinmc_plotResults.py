def plotResults(lat,lon, selectedScene,sceneDf,imagePath):
    #prepare a plot
    plt.figure()

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