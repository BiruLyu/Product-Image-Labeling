import cv2
import numpy as np

img = cv2.imread('001.jpg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT()
kp, des = sift.detectAndCompute(gray,None)

print len(kp)
#print kp,des
