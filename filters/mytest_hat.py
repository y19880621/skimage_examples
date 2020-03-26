from skimage import data, color
import matplotlib.pyplot as plt
from skimage.morphology import disk
import skimage.filters.rank as sfr

img = color.rgb2gray(data.camera())
bh = sfr.bottomhat(img, disk(5))  # 半径为5的圆形滤波器
th = sfr.tophat(img, disk(5))

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 8))
axes = axes.ravel()
ax0, ax1, ax2, ax3 = axes

ax0.imshow(img, cmap=plt.cm.gray, interpolation='nearest')
ax0.set_title("Original")
ax2.imshow(bh, cmap=plt.cm.gray, interpolation='nearest')
ax2.set_title("Bottomhat")
ax3.imshow(th, cmap=plt.cm.gray, interpolation='nearest')
ax3.set_title("Tophat")

for ax in axes:
    ax.axis('off')

fig.tight_layout()
plt.show()
