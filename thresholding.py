import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread(r"C:\Users\ADMIN\sample.jpeg.jfif")
cv.imshow('Cat',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#simple thresholding
threshold,thresh=cv.threshold(gray,100,255,cv.THRESH_BINARY)
cv.imshow('Simple Threshold',thresh)

threshold,thresh_inv=cv.threshold(gray,100,255,cv.THRESH_BINARY_INV)
cv.imshow('Inverse Threshold',thresh_inv)

#adaptive thresholding
adap=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,1)
cv.imshow("Adaptive Thresholding",adap)



cv.waitKey(0)