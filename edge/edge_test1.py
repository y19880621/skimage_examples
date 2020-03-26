from skimage import data, filters
import matplotlib.pyplot as plt

img = data.camera()

# edges = filters.sobel(img)
# edges = filters.roberts(img)
# edges = filters.scharr(img)
edges = filters.prewitt(img)

# plt.figure('canny', figsize=(8, 8))
plt.imshow(edges, plt.cm.gray)
plt.show()
