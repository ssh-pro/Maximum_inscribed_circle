# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 22:37:26 2019

@author: shinnkun
"""

import cv2
import numpy as np
import os
from numba.decorators import jit


def cuter(imgpath,exitpath,l):    
    imgray = cv2.imread(imgpath,0)
    ret, thresh = cv2.threshold(imgray, 1, 255, 0)
    #ret, thresh = cv2.threshold(a, 1, 255, 0)
    contours = cv2.findContours((thresh), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[1]
    for i, contour in enumerate(contours):
            # 小さな領域の場合は間引く
            area = cv2.contourArea(contour)
            if area < 500:
                continue
        # 
            if 11000*11000 * 0.4 < area:
                continue
        
        # 外接矩形を取得
            x,y,w,h = cv2.boundingRect(contour)
            target = thresh[y:y+h,x:x+w]
    l.append(path)
    l.append([x,w,y,h])
    cv2.imwrite(exitpath,target)
    return l

def pixel_del(path,exname,size):     
    im = cv2.imread(path)
    im=cv2.bitwise_not(im)
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    bimg=cv2.adaptiveThreshold(gray, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,2 )
    image,contours,hierarchy = cv2.findContours(bimg,cv2.RETR_EXTERNAL|cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    new_contours=[]
    FILL_COLOR=(0,0,0)
    AREA_MAX=size    
    for c in contours:
        s=abs(cv2.contourArea(c))
        if s <= AREA_MAX:
            new_contours.append(c)
    cv2.drawContours( im, new_contours, -1,FILL_COLOR,-1)
    cv2.imwrite(exname,im)

####################################################################
"""
f=os.listdir("im")
f=[a for a in f if ".png" in a and "._" not in a]
g=[]
for path in f:
    cuter("im//"+path,"sh//"+path,g)

f=os.listdir("sh")
f=[a for a in f if ".png" in a and "._" not in a]
g=[]
for path in f:
    wa("sh//"+path,"del//"+path,500)


f=os.listdir("del")
f=[a for a in f if ".png" in a and "._" not in a]
g=[]
for path in f:
    wa("del//"+path,"del1//"+path,500)
"""
