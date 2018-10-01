import numpy as np
import cv2
from matplotlib import pyplot as plt
def mean_list(l):
    n,s=0,0
    for row in l:
        s+=sum(row)
        n+=len(row)
    return float(s)/n
def median_list(l):
    n=0
    x=[]
    for row in l:
        n+=len(row)
        for i in row:
            x.append(i)
    x.sort()
    return x[n/2]
def mode_list(l):
    di={}
    for row in l:
        for i in row:
            if i not in di:
                di[i]=1
            else:
                di[i]=di[i]+1
    x=-1
    mode=-1
    for i in di:
        if di[i]>x:
            x=di[i]
            mode=i
    return mode
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread('13.jpg')
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
data=[]
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    #data.append((y,mean_list(roi_gray),median_list(roi_gray),mode_list(roi_gray)))
    roi_color = img[y:y+h, x:x+w]
    print y
    histr = cv2.calcHist([roi_gray],[0],None,[256],[0,256])
    plt.plot(histr)
    #plt.show()
plt.show()
#for i in data:
    #print "Y",i[0],"Mean",i[1],"Median",i[2],"Mode",i[3]
cv2.namedWindow('img',cv2.WINDOW_NORMAL)
cv2.resizeWindow('img',1000,1000)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
