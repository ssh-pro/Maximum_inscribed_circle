#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 17:38:13 2019
@author: joil
http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html  
"""

import cv2
import numpy as np
from numba.decorators import jit

@jit
def wa(comp,exdir1,size):
    path=comp     
    im = cv2.imread(path)
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    bimg=cv2.adaptiveThreshold(gray, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,2 )
    image,contours,hierarchy = cv2.findContours(bimg,cv2.RETR_EXTERNAL|cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    new_contours=[]
    FILL_COLOR=(255,255,255)
    AREA_MAX=size    
    for c in contours:
        s=abs(cv2.contourArea(c))
        if s <= AREA_MAX:
            new_contours.append(c)
    cv2.drawContours( im, new_contours, -1,FILL_COLOR,-1)
    cv2.imwrite(exdir1,im)

def circle_checker(centerX,centerY,location):
    l=[]
    for x,y in  location:
        radius=np.sqrt((y-centerY)**2+(x-centerX)**2)
        l.append(radius)
    return l


@jit
def image_location(img):
    res=[]
    for y in range(0,np.shape(img)[0]):
        for x in range(0,np.shape(img)[1]):
            a=[]
            color=img[y][x]
            b=color[0]
            g=color[0]
            r=color[0]
            if b != 255:
                a.append(x)
                a.append(y)
                res.append(a)
            else:
                pass
    return res

a=cv2.imread("1.png")

imgray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray, 1, 255, 0)
#ret, thresh = cv2.threshold(a, 1, 255, 0)

contours = cv2.findContours((thresh), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[1]
dst=a
for i, contour in enumerate(contours):
        # 小さな領域の場合は間引く
        area = cv2.contourArea(contour)
        if area < 500:
            continue
        # 画像全体を占める領域は除外する
        if 11000*11000 * 0.4 < area:
            continue        
        # 外接矩形を取得
        x,y,w,h = cv2.boundingRect(contour)
        target = thresh[y:y+h,x:x+w]


"""
a=cv2.imread("daen.jpg")
d=circle_writer(421,171,400,80,30)
cv2.imwrite("dda.jpg",d)
loc=[]
d=cv2.imread("dda.jpg")
loc=image_location(d)


f=os.listdir("sh")
ddd=[path for path in f if ".png" in path]
for path in ddd:
    pa="sh//"+path
    a=cv2.imread(pa,0)
    a=cv2.bitwise_not(a)
    
    kernel = np.ones((6,6),np.uint8)
    opening = cv2.morphologyEx(a, cv2.MORPH_OPEN, kernel)
    cv2.imwrite("del1//"+path,a)
    cv2.imwrite("del//"+path,opening)
    l=cv2.imread("del//"+path)
    wa(("del//"+path),("fff//"+path),10)
"""
