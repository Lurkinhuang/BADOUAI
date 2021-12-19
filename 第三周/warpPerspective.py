import cv2
import numpy as np
# Method 1
#读取图像,将原图转为灰度图
img = cv2.imread("book.jpg", 0)
h, w = img.shape
src = np.array([[496, 181], [1246, 467], [832, 1480], [138, 1085]], dtype='float32')
sdt = np.array([[0, 0], [1000, 0], [1000, 1000], [0, 1000]], dtype='float32')

#计算变换矩阵
matrix = cv2.getPerspectiveTransform(src, sdt)
print(matrix)

#计算透视变换后的图片
perspective_img = cv2.warpPerspective(img, matrix, (1000, 1000))
cv2.imshow("perspective_img", perspective_img)
cv2.waitKey(0)


# # Method 2
# def warp_matrix(src, sdt):
