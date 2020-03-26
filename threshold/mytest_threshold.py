from skimage import data, color, filters
import matplotlib.pyplot as plt
from skimage.morphology import disk
import skimage.filters.rank as sfr

original_image = color.rgb2gray(data.camera())
plt.imshow(original_image, cmap=plt.cm.gray)

thresh = []
thresh.append(filters.threshold_otsu(original_image))
thresh.append(filters.threshold_yen(original_image))
thresh.append(filters.threshold_li(original_image))
thresh.append(filters.threshold_isodata(original_image))

filtered_images = []
for t in thresh:
    dst = (original_image <= t) * 1.0  # 根据阈值进行分割
    filtered_images.append(dst)

name_list = ['otsu', 'yen', 'li', 'isodata']

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 8))
axes = axes.ravel()
for ax, img, name in zip(axes, filtered_images, name_list):
    ax.imshow(img, cmap=plt.cm.gray, interpolation='nearest')
    ax.set_title(name)

for ax in axes:
    ax.axis('off')

fig.tight_layout()
plt.show()