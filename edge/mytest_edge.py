from skimage import data, color, filters
import matplotlib.pyplot as plt
from skimage.morphology import disk
import skimage.filters.rank as sfr

original_image = color.rgb2gray(data.camera())
plt.imshow(original_image, cmap=plt.cm.gray)

filtered_images = []
filtered_images.append(filters.sobel(original_image))
filtered_images.append(filters.roberts(original_image))
filtered_images.append(filters.scharr(original_image))
filtered_images.append(filters.prewitt(original_image))

name_list = ['sobel', 'roberts', 'scharr', 'prewitt']

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 8))
axes = axes.ravel()
for ax, img, name in zip(axes, filtered_images, name_list):
    ax.imshow(img, cmap=plt.cm.gray, interpolation='nearest')
    ax.set_title(name)

for ax in axes:
    ax.axis('off')

fig.tight_layout()
plt.show()