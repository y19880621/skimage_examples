from skimage import data, color
import matplotlib.pyplot as plt
from skimage.morphology import disk
import skimage.filters.rank as sfr

original_image = color.rgb2gray(data.camera())
plt.imshow(original_image, cmap=plt.cm.gray)

filtered_images = []
filtered_images.append(sfr.autolevel(original_image, disk(5)))
filtered_images.append(sfr.bottomhat(original_image, disk(5)))
filtered_images.append(sfr.tophat(original_image, disk(5)))
filtered_images.append(sfr.enhance_contrast(original_image, disk(5)))
filtered_images.append(sfr.entropy(original_image, disk(5)))
filtered_images.append(sfr.equalize(original_image, disk(5)))
filtered_images.append(sfr.gradient(original_image, disk(5)))
filtered_images.append(sfr.maximum(original_image, disk(5)))
filtered_images.append(sfr.minimum(original_image, disk(5)))
filtered_images.append(sfr.mean(original_image, disk(5)))
filtered_images.append(sfr.median(original_image, disk(5)))
filtered_images.append(sfr.modal(original_image, disk(5)))
filtered_images.append(sfr.otsu(original_image, disk(5)))
filtered_images.append(sfr.threshold(original_image, disk(5)))
filtered_images.append(sfr.subtract_mean(original_image, disk(5)))
filtered_images.append(sfr.sum(original_image, disk(5)))

name_list = ['autolevel', 'bottomhat', 'tophat', 'enhance_contrast', 'entropy', 'equalize', 'gradient',
             'maximum', 'minimum', 'mean', 'median', 'modal', 'otsu', 'threshold', 'subtract_mean', 'sum']

fig, axes = plt.subplots(nrows=4, ncols=4, figsize=(8, 8))
axes = axes.ravel()
for ax, img, name in zip(axes, filtered_images, name_list):
    ax.imshow(img, cmap=plt.cm.gray, interpolation='nearest')
    ax.set_title(name)

for ax in axes:
    ax.axis('off')

fig.tight_layout()
plt.show()