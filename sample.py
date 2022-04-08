import cv2 as cv
img=cv.imread(r"C:\Users\ADMIN\sample.jpeg.jfif")

cv.imshow('Cat',img)
#capture = cv.VideoCapture(r"D:\Downloads folder\Dog.mp4")
def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1] * scale)
    height =int(frame.shape[0] * scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

f=rescaleFrame(img,scale=0.5)
cv.imshow('Cat resized',f)
cv.waitKey(0)
