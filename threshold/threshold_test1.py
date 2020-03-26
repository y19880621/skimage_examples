from skimage import data, filters
import matplotlib.pyplot as plt

image = data.camera()

# thresh = filters.threshold_otsu(image)  # 返回一个阈值
# thresh = filters.threshold_yen(image)
# thresh = filters.threshold_li(image)
thresh = filters.threshold_isodata(image)

dst = (image <= thresh) * 1.0  # 根据阈值进行分割

plt.figure('thresh', figsize=(8, 8))

plt.subplot(121)
plt.title('original image')
plt.imshow(image, plt.cm.gray)

plt.subplot(122)
plt.title('binary image')
plt.imshow(dst, plt.cm.gray)

plt.show()
