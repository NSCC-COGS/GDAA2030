# print ('hello world')
import scipy, numpy                     #import math library (numpy), and the toolkit scipy
import matplotlib 
from matplotlib import pyplot as plt    # plotting library that can be used to plot graphs

#Displaying the image to screen code, this allows us to display an aerial image from the same folder as 
#the code
imagePath = 'tutorial1Image.png'
im = plt.imread(imagePath,format= None)  #open the tutorial image, using the imread function to view image
imarray = numpy.array(im)           #convert the image to a numpy array
print (imarray)                     # display to confirm that the image is loaded into the computer
plt.imshow(imarray)                #display/plot the image from the array
plt.show()                          #display the image in a seperate screen

#In class work

# print (imarray[12, 43, 0])              # indexing which allows you to print just the first band of the array. 
r = imarray[:,0,0]                     #set each band as a specific variable
g = imarray[:,0,1]
b = imarray[:,0,2]
alpha = imarray[:,:,-1]                 #-1 is the last row and so this can get you the last rows

imarray_new = (r - b) / (b + r)             #plot the bands and then show them
plt.plot(r, c= "red")
plt.plot(g, c= "green")
plt.plot(b, c = "blue")
plt.plot(imarray_new, c= "pink")
plt.show()

plt.scatter(b,r, c= "red", linewidth = 0, alpha = .2)     #make a scatter plot to see the data, alpha and line width make it coloured to see clusters
plt.show()
# for i in range (0, imarray.shape[2]):
#     for j in range (i,imarray.shape[1]-1):
#         for k in (0,imarray.shape[2]-1):
#             print (k,j,i)
#             print (imarray[i,j,k])
#             input()

# for x in numpy.nditer(imarray):            #this is a generator for each array information
#     print(x)


#Tutorial 1 continued from the PDF
#Create and display a histogram

ImarrayRED = imarray[:,:,0]             #turn the image into one image band (only red)
ImarrayRED_1D = ImarrayRED.flatten()    #create one dimensional array
plt.hist (ImarrayRED_1D, bins=20)       #This creates a histogram of the red band which is then displayed
plt.show()

#Display the histogram and image band in the same window
plt.subplot(2,1,1)                      
plt.imshow(ImarrayRED, cmap="gray")     #turn the image into a grayscale image
plt.subplot(2,1,2)                      #this helps to graph the images so that the histogram is below the image
plt.hist(ImarrayRED_1D,bins=20)
plt.show()

#Multiple Data in a Loop

bands = [0,1,2]                                  #creates a list for each of the bands

plt.figure(num='kmaynard')                       #name the figure

for index in bands:                               #create a grayscale image and histogram for each band for the image  
    plt.subplot(2,3, index +1)
    plt.imshow(imarray[:,:,index], cmap="gray")
    plt.subplot(2,3,index+1+3)
    plt.hist(imarray[:,:,index].flatten(),bins=20)
plt.show()                                          #display all looped bands into one image