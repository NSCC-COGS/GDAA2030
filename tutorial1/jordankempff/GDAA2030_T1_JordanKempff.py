# import the libraries
import scipy, numpy
from matplotlib import pyplot

# pull the image from the computer
image = pyplot.imread(r"tutorial1Image.png")

# take an array of the image
arr = numpy.array(image)

# take the bands 0, 1, and 2 
Bands = [0,1,2]

# assign a title to the window
pyplot.figure(num='Jordan J Kempff')

# begin a loop
for index in Bands:

    # show the bands in grayscale
    pyplot.subplot(2,3, index +1)
    pyplot.imshow(arr[:,:,index], cmap="gray")

    # flatten the bands
    pyplot.subplot(2,3, index+1+3)
    pyplot.hist(arr[:,:,index].flatten(), bins=20)

# show the subplot
pyplot.show()