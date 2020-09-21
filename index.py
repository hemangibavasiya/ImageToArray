from skimage import io
import matplotlib.pyplot as plt
import numpy as np
photo = io.imread('image006.png')
print(photo.shape)
plt.imshow(photo)
print(plt.imshow(photo))
print(np.sin(photo))
