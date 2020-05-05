# ----------------------------------------------------------
# program title: tutorial one 
# file name: GDAA2030_T1_benmanthorne.py 
# date: 2/4/2020 
# name: ben manthorne
# ----------------------------------------------------------

# import the numpy and matplotlib libraries
import numpy as np
import matplotlib

# importing pyplot from matplotlib
from matplotlib import pyplot as plt 

# setting the tutorial image as "image"
# it is contained within the same folder as the script
image = plt.imread('tutorial1sample.png')

# getting the image data as an array 
arr = np.array(image) 

# setting bands as the array values 
Bands = [0,1,2]

# naming the figure after myself 
plt.figure(num = 'ben manthorne')

# per item in the bands list, show the appropriate band 
# in gray scale, then show a histogram related to it 
# below that image 
for index in Bands: 

    plt.subplot(2,3, index +1)
    plt.imshow(arr[:,:,index], cmap = 'gray') 
    plt.subplot(2,3, index+1+3) 
    plt.hist(arr[:,:,index].flatten(), bins=20) 

# show the images and histograms 
plt.show() 