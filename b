#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 21:36:42 2019

@author: joil
"""
import cv2
import numpy as np
from numba.decorators import jit

@jit
def circle_checker(centerX,centerY,x,y):
    radius=np.sqrt((y-centerY)**2+(x-centerX)**2)
    return radius

def image_location(img,mode):
    if mode ==1:
        img=img
    else:
        img=cv2.imread(img)
        
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


#線画にした
mv=cv2.imread("output.jpg",0)
ret,thresh1 = cv2.threshold(mv,127,255,cv2.THRESH_BINARY)
cv2.imwrite("tes.jpg",thresh1)


#choose which image u d like to use
#どちらにしろ三平方の丸め誤差が聞いてきます
#1 輪郭に厚みがあります
#image_location=image_location("daen.jpg",0)

#2 厚みはありません
image_location=image_location("tes.jpg",0)

cx=200
cy=50
cr=20


for a in l2:
    print(a[0])
    print(a[1])

#一つのRについて
#l2=[]
while len(l2) < 3:
    cr=cr+1
    l2=[]
    for x,y in image_location:
        if np.abs(cr - (circle_checker(cx,cy,x,y))) < 2:
            l=[]
            l.append(x)
            l.append(y)
            l2.append(l)
        else:
            pass
#appendしたら,X,Yを2ほど進めてやる
#そうすれば一個だけもとまる




