# -*- coding: utf-8 -*-
from scipy.misc import imresize
import graphcut
import os
from PIL import Image
from pylab import *
import cv2

img = cv2.imread('018.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

contoures, hierarchy = cv2.findContours(binary,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
areas = np.zeros(len(contoures))
idx = 0
for cont in contoures :
    areas[idx] = cv2.contourArea(cont)
    idx = idx + 1
areas_s = cv2.sortIdx(areas, cv2.SORT_DESCENDING | cv2.SORT_EVERY_COLUMN)
print areas_s

# (b8, g8, r8) = cv2.split(img)
#
# # 对每个区域进行处理
# for idx in areas_s :
#     if areas[idx] < 100 :
#         break
#
#     # 绘制区域图像，通过将thickness设置为-1可以填充整个区域，否则只绘制边缘
#     poly_img = np.zeros(img.shape, dtype = np.uint8 )
#     cv2.drawContours(poly_img, contoures, idx, [255,255,255], -1)
#     poly_img = poly_img & img
#
#     # 得到彩色的图像
#     color_img = cv2.merge([b8 & poly_img, g8 & poly_img, r8 & poly_img])
#
#     cv2.imshow('poly_img', color_img)
#     cv2.waitKey()

for idx in areas_s :
    if areas[idx] < 100:
        break

    #poly_img = np.zeros(img.shape, dtype = np.uint8 )
    #print contoures
    cv2.drawContours(img,contoures,idx,(0,0,0),-1)

    cv2.imshow("img", img)
    cv2.waitKey(0)
