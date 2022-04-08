import cv2 as cv
import numpy as np
blank=np.zeros((400,400),dtype='uint8')

rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('Rectangle',rectangle)
cv.imshow('Circle',circle)

#bitwise_and

bitwise_and=cv.bitwise_and(rectangle,circle)
cv.imshow('AND',bitwise_and)
#bitwise_or
bitwise_or=cv.bitwise_or(rectangle,circle)
cv.imshow('OR',bitwise_or)
#bitwise_xor
bi=cv.bitwise_xor(rectangle,circle)
cv.imshow('XOR',bi)
#bitwise
bi1=cv.bitwise_not(circle)
cv.imshow('NOT',bi1)
cv.waitKey(0)