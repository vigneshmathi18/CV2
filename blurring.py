import cv2 as cv
import numpy as np
img=cv.imread(r"C:\Users\ADMIN\sample.jpeg.jfif")
#cv.imshow('Cat',img)
#averaging
average=cv.blur(img,(7,7))
cv.imshow('average blur',average)

#gaussian blur
blur=cv.GaussianBlur(img,(7,7),0)
cv.imshow('Gaussoian Blur',blur)

#Medain blur
m_blur=cv.medianBlur(img,7)
cv.imshow('Medain Blur',m_blur)

#bilateral
bi=cv.bilateralFilter(img,10,15,15)
cv.imshow('Bilateral Blur',bi)



cv.waitKey(0)