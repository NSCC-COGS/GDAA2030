import numpy as np
from matplotlib import pyplot as plt

image = plt.imread(r"tutorial1Image.PNG")

arr = np.array(image)

Bands = [0,1,2] 

plt.figure(num='kevin k mcguigan')

for index in Bands: 

	plt.subplot(2,3, index +1)
	plt.imshow(arr[:,:,index], cmap="gray")
	plt.subplot(2,3, index+1+3)
	plt.hist(arr[:,:,index].flatten(),bins=20) 

plt.show()