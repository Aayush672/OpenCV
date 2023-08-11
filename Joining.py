import cv2
import numpy as np
img1 = cv2.imread("Downloads/BGMI.jpg")
img2 = cv2.imread("Downloads/aashman.jpg")

imgHor = np.hstack((img1,img2))
imgVer = np.vstack((img2,img1))
cv2.imshow("Horizontal",imgHor)
cv2.imshow("Vertical",imgVer)
cv2.waitKey(0)