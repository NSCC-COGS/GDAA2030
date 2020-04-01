import numpy as np
from matplotlib import pyplot

''' lets show 3 bands of an image and histograms'''

image = pyplot.imread(r"tutorial1Image.PNG")



arr = np.array(image)

# input()


# r = arr[0:20,0:20,0]
# g = arr[0:20,0:20,1]
# b = arr[0:20,0:20,2]
r = arr[:,:,0]
g = arr[:,:,1]
b = arr[:,:,2]

pyplot.subplot(2,1,1)
r_1D = r.flatten()
pyplot.hist(r_1D, bins=20) 
pyplot.subplot(2,1,2)
pyplot.imshow(r, cmap = 'gray')
pyplot.show()

r_1D = r.flatten()
pyplot.hist(r_1D, bins=20) 

g_1D = r.flatten()
pyplot.hist(g_1D, bins=20) 

b_1D = r.flatten()
pyplot.hist(b_1D, bins=20) 


pyplot.show()

'''

arr_new = (r - b) / (b + r)

pyplot.scatter(b, r, c='red', linewidth = 0 , alpha = .2)
# pyplot.plot(g, c='green')
# pyplot.plot(b, c='blue')
# pyplot.plot(arr_new, c='pink')

pyplot.show()
'''
# for x in np.nditer(arr):
#     print(x)

# input('wait up...')

# pyplot.imshow(r, cmap = 'gray')
# pyplot.show()

# print('hello')