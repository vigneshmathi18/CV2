import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread(r"C:\Users\ADMIN\sample.jpeg.jfif")
cv.imshow('Cat',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

blank=np.zeros(img.shape[:2],dtype='uint8')
circle=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)

mask=cv.bitwise_and(img,img,mask=circle)
cv.imshow('Mask',mask)

#histograms grayscale
gr_hist=cv.calcHist([gray],[0],mask,[256],[0,256])
plt.figure()
plt.title("Grayscale Histogram ")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.plot(gr_hist)
plt.xlim([0,256])
plt.show()

#color histogram
plt.figure()
plt.title("Color Histogram ")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
color=('b','g','r')
for i,col in enumerate(color):
    hist=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)