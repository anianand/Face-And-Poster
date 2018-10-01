import imutils
import numpy as np
import argparse
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
lower = np.array([0, 48, 80], dtype = "uint8")
upper = np.array([20, 255, 255], dtype = "uint8")
frame=cv2.imread("4.jpg")
converted = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
skinMask = cv2.inRange(converted, lower, upper)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
skinMask = cv2.erode(skinMask, kernel, iterations = 2)
skinMask = cv2.dilate(skinMask, kernel, iterations = 2)
skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)
skin = cv2.bitwise_and(frame, frame, mask = skinMask)
gray=cv2.cvtColor(skin, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    img = cv2.rectangle(skin,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = skin[y:y+h, x:x+w]
cv2.namedWindow('images',cv2.WINDOW_NORMAL)
cv2.resizeWindow('images',1200,1000)
cv2.imshow("images",np.hstack([frame,skin]))
cv2.waitKey(0)
cv2.destroyAllWindows()
