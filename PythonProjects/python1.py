import numpy as np
import matplotlib as plt
import cv2

img=cv2.imread(r"C:/Users/NITRO5/Desktop/1.jpg",cv2.IMREAD_GRAYSCALE)

cv2.imshow('img',img)
cv2.waitKey()
plt.hist(img.ravel(),255,[0,255])
plt.show()
equl_img=cv2.equalizeHist(img)
cv2.imshow('equilized image',equl_img)
cv2.waitKey()
plt.hist(equl_img.ravel(),255,[0,255])
plt.show()