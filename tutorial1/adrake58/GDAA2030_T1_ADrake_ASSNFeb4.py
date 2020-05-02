#==================================
# Tutorial 1 Image Analytics
# Introduction to Python GDAA2030
# A.Drake  Jan 28 2020
#=================================


print ('hello world')
import numpy as np
from matplotlib import pyplot
# show 3 band of an image an histograms

image = pyplot.imread(r"tutorial1Image.PNG")

arr = np.array(image)

# shows characteristics/shape of array
# print(arr.shape)
# input()

# a form of clipping choose spec pixels to show
# r = arr[0:100,0:100,0]
# g = arr[0:100,0:100,1]
# b = arr[0:100,0:100,2]

#double colon skips a certain number of pixels
# r = arr[::100,:,0]
# g = arr[::100,:,1]
# b = arr[::100,:,2]

r = arr[:,:,0]
g = arr[:,:,1]
b = arr[:,:,2]

pyplot.subplot(2,1,1,)
r_1D = r.flatten()
pyplot.hist(r_1D,bins=20)
pyplot.subplot(2,1,2)
pyplot.imshow(r, cmap = 'gray')



#  : means everything
# types are same for an array

# r = arr[:,:,0]
# g = arr[:,:,1]
# b = arr[:,:,2]

#alpha channel transparent
# alpa = arr[:,:,-1]




# arr_new = (r -b) / (b + r)

# pyplot.plot(r, c='red')
# pyplot.plot(g, c='green')
# pyplot.plot(b, c='blue')

# pyplot.scatter(b,r, c='red', linewidths= 0, alpha= .2)




#for x in np.nditer(arr):
#   print (x)

#input('stop doing stuff...')

#pyplot.imshow(image)
pyplot.show()


