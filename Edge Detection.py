import cv2 as cv
import numpy as np
img=cv.imread(r"C:\Users\ADMIN\sample.jpeg.jfif")
cv.imshow('Cat',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#laplacian
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow('LAP',lap)

#sabel
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
comined=cv.bitwise_or(sobelx,sobely)
cv.imshow('SOBELx',sobelx)
cv.imshow('SOBELy',sobely)
cv.imshow('SOBEL combined',comined)

canny=cv.Canny(gray,150,175)
cv.imshow("Canny",canny)

cv.waitKey(0)