from skimage import data, color
import matplotlib.pyplot as plt
from skimage.morphology import disk
import skimage.filters.rank as sfr

img = color.rgb2gray(data.camera())

# auto = sfr.autolevel(img, disk(5))
# auto = sfr.bottomhat(img, disk(5))
# auto = sfr.tophat(img, disk(5))
# auto = sfr.enhance_contrast(img, disk(5))
# auto = sfr.entropy(img, disk(5))
# auto = sfr.equalize(img, disk(5))
# auto = sfr.gradient(img, disk(5))
# auto = sfr.maximum(img, disk(5))
# auto = sfr.minimum(img, disk(5))
# auto = sfr.mean(img, disk(5))
# auto = sfr.median(img, disk(5))
# auto = sfr.modal(img, disk(5))
# auto = sfr.otsu(img, disk(5))
# auto = sfr.threshold(img, disk(5))
# auto = sfr.subtract_mean(img, disk(5))
auto = sfr.sum(img, disk(5))

plt.figure('filters', figsize=(8, 8))
plt.subplot(121)
plt.title('origin image')
plt.imshow(img, plt.cm.gray)

plt.subplot(122)
plt.title('filted image')
plt.imshow(auto, plt.cm.gray)
plt.show()
