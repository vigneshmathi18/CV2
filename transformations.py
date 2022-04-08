import numpy as np
import cv2 as cv
img=cv.imread(r"C:\Users\ADMIN\sample.jpeg.jfif")
cv.imshow('Cat',img)

#translation
def translate(img,x,y):
    transMat=np.float32([[1, 0, x],[0, 1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)
translated=translate(img,-100,-100)
cv.imshow('translated',translated)

#rotation
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]
    if rotPoint is None:
        rotPoint=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)

    return cv.warpAffine(img,rotMat,dimensions)

rotated=rotate(img,-90)
cv.imshow('rotated',rotated)

#resize
#resize
resize=cv.resize(img,(500,400),interpolation=cv.INTER_AREA)
cv.imshow('Resizing',resize)

#flipping
flip=cv.flip(img,-1)
cv.imshow('Flipping',flip)
cv.waitKey(0)