import cv2 as cv
img=cv.imread(r"C:\Users\ADMIN\sample.jpeg.jfif")
cv.imshow('Cat',img)
#gray scale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Cat gray',gray)
#blur image
blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#Edge Cascadde
canny=cv.Canny(img,125,175)
cv.imshow('Canny',canny)
#dialate
dilate=cv.dilate(canny,(3,3),iterations=1)
cv.imshow('Dialated Edges',dilate)

#eroding
erding=cv.erode(dilate,(3,3),iterations=2)
cv.imshow('Eroding',erding)

#resize
resize=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('Resizing',resize)
cv.waitKey(0)