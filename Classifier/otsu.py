# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt


# 使用2g-r-b分离土壤与背景

src = cv2.imread('C:\\Users\\RubyLyu\\PycharmProjects\\PictureDB\\Taobao\\518.jpg')
cv2.imshow('src', src)


# 转换为浮点数进行计算
fsrc = np.array(src, dtype=np.float32) / 255.0
(b,g,r) = cv2.split(fsrc)
gray = 2 * g - b - r

# 求取最大值和最小值
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)

# 计算直方图
hist = cv2.calcHist([gray], [0], None, [256], [minVal, maxVal])
plt.plot(hist)
plt.show()

cv2.waitKey()

# 转换为u8类型，进行otsu二值化
gray_u8 = np.array((gray - minVal) / (maxVal - minVal) * 255, dtype=np.uint8)
(thresh, bin_img) = cv2.threshold(gray_u8, -1, 255,cv2.THRESH_OTSU)
#bin_img = cv2.adaptiveThreshold(gray_u8,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,13,2)
bin_img = cv2.bitwise_not(bin_img)
#contoures, hierarchy = cv2.findContours(bin_img,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#cv2.drawContours(bin_img,contoures,-1,(0,0,0),-1)
count = 0
count2 = 0
x = bin_img.shape[0]/8
y = bin_img.shape[1]/8

for i in range(3*x,5*x):
    for j in range(3*y,5*y):
        if bin_img[i,j] == 255:
            count = count + 1
        count2 = count2 + 1
print count,count2

# if count > 4000:
#     for i in range(8*x):
#         for j in range(8*y):
#             if bin_img[i,j] == 0:
#                 bin_img[i,j] = 255
#             else:
#                 bin_img[i,j] = 0


img=np.zeros((800,800,1), np.uint8)
cv2.rectangle(img,(300,300),(500,500),(0,255,0))
cv2.imshow('bin_img', img)
cv2.imshow('bin_img', bin_img)
cv2.waitKey()

# 得到彩色的图像
(b8, g8, r8) = cv2.split(src)
color_img = cv2.merge([b8 & bin_img, g8 & bin_img, r8 & bin_img])
cv2.imshow('color_img', color_img)
cv2.waitKey()

