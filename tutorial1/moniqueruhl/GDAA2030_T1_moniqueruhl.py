'''
Script Name  : GDAA2030_T1_moniqueruhl.py
Purpose      : Intro to python for image analytics
Written By   : M Ruhl, 2020.02.04
'''
#importing required libraries
import scipy
import numpy as np 

from matplotlib import pyplot as plt #python's 2D plotting library 
from PIL import Image #python's image library


#Displaying the Image to the Screen
#==================================
#imPath=(r'ship.PNG') #set variable for image, load image using 'r' to interpret string literally, no escape key issues if full file path is used
imPath=(r'F:\COGS\GDAA2030\ship.PNG') #example of file from different location
im=Image.open(imPath)
imArr=np.array(im)
print(imArr)
print('Size of my image array =' , imArr.shape) #finding out the size of my array with numpy function
plt.imshow(imArr)
plt.show() #show array


#Displaying a Historgram
#=======================
imArrRed=imArr[:,:,0] #reduce image to single band [x,y,n] where x=select all in array, y=select all in array, n=0
imArrRed_1D=imArrRed.flatten() #flatten data to a one-dimensional array for pyplot plots

plt.hist(imArrRed_1D, bins=20) #using matplotlib to compute history of 1D array, set to 20 bins
plt.title("Histogram of red band") #create title for histogram
plt.show() #show histogram 

#show red band histogram and image in same figure
plt.subplot(2,1,1) #figure with 2 rows, 1 column, show subplot at index position 1
plt.imshow(imArrRed,cmap="gray") #show image in grayscale
plt.subplot(2,1,2) #show subplot at index position 2
plt.hist(imArrRed_1D,bins=20) 
plt.show()


#Displaying Multiple Data in a Loop
#==================================
bands=[0,1,2] #create list to represent R G B rows in PNG image

plt.figure(num='Monique Ruhl') #put name in top corner of figure

#create loop to add each R G B histogram and grayscale images into one figure
for index in bands:
    plt.subplot(2,3,index+1) #figure with 2 rows, 3 columns, show subplots at index position index+1
    plt.imshow(imArr[:,:,index],cmap="gray") 
    plt.title('Band number= %s' % index)
    plt.subplot(2,3,index+1+3) #show subplots at index position index+1+3
    plt.hist(imArr[:,:,index].flatten(),bins=20)

plt.show()