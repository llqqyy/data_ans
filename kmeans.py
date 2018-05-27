from skimage import io
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

img = io.imread('C:/Users/刘青源/Desktop/dog.png')
img_x = img.shape[0]
img_y = img.shape[1]
data = []
for i in range(img_x):
    for j in range(img_y):
        x = img[i, j, 0]
        y = img[i, j, 1]
        z = img[i, j, 2]
        data.append([x / 255, y / 255, z / 255])
label = KMeans(n_clusters=6).fit_predict(data)
label = label.reshape([img_x, img_y])
newimg = np.zeros((img_x, img_y, 3))
for i in range(img_x):
    for j in range(img_y):
        a = float(256 / (label[i][j] + 1) - 5)
        newimg[i, j, 0] = int(a) + 30
        newimg[i, j, 1] = int(a) + 20
        newimg[i, j, 2] = int(a) - 5
plt.figure("new")  # 窗口命名
print(newimg)
plt.imshow(newimg)
plt.show()  # 显示图像
