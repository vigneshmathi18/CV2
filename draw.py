import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')
#cv.imshow('Blank',blank)

#paint the image with certain colour
#blank[:]=0,0,255
#cv.imshow('Green',blank)
#Draw a rectangle
cv.rectangle(blank,(0,0),(250,250),(0,0,255),thickness=2)
cv.imshow('Rectangle',blank)
#Draw a circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1)
cv.imshow('Circle',blank)
#Draw a line
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,255),thickness=3)
cv.imshow('line',blank)
#Write Text
cv.putText(blank,'VIGNESH', (255,255),cv.FONT_ITALIC,1.0,(0,255,252),thickness=3)
cv.imshow('text',blank)
#img=cv.imread(r"C:\Users\ADMIN\sample.jpeg.jfif")
#cv.imshow('Cat',img)
cv.waitKey(0)