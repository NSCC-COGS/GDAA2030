########################################################################
### Purpose:    Image Analytics - Assignment 1                       ###
### Name:       M Kirby                                              ###
### Date:       Feb 11 2020                                          ###
########################################################################

# import libraies
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image


# set variable to our selected image (stored locally)
imagePath = 'GDAA2030_T1_Kirby.png'

# creates a variable as a pillow object from image
im = Image.open(imagePath)

# ceates a variable as a numpy array from the pillow object
imarray = np.array(im)

# a list of the available bands in the image, would be more in a MS/HS image
bands = [0,1,2]

# declaring the figure object pror to the loop to title it
plt.figure(num='Mark Kirby - Assignment 1')

# loop through the bands and creates a 2 x 3 array of subplots
# the first row is an image of a single band from the image
# the second row is a histogram of each band in the image
# ADDITIONAL: Added titles to each subplot, adjusted spacing for nicer output
for index in bands:

    # first row of the subplot: index +1 results in first, second, third subpot
    plt.subplot(2,3, index+1)
    plt.title('Band ' + str(index+1))
    plt.imshow(imarray[:,:,index], cmap="gray")

    # second row of the subplot: index +1 +3 results in fourth, fifth, sixth subplot
    plt.subplot(2,3,index+1+3)
    plt.title('Band ' + str(index+1))
    plt.hist(imarray[:,:,index].flatten(), bins=20)

    # adjust some spacing for more nicer output
    plt.subplots_adjust(wspace=.3, hspace=.3)

# opens the populated plot window
plt.show()