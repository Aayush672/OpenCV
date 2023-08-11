import cv2
import numpy as np
img = cv2.imread("Desktop/BGMI.jpg")
print(img.shape)
imgResize = cv2.resize(img,(500,1000))
print(imgResize.shape)
imgCrop = img[0:200,200:500]
print(imgCrop.shape)
cv2.imshow("Image",img)
cv2.imshow("Resized Image",imgResize)
cv2.imshow("Crooped Image",imgCrop)
cv2.waitKey(0)