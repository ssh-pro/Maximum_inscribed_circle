#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 21:52:26 2019

@author: joil
"""
import cv2
import numpy as np
from numba.decorators import jit


@jit
def circle_checker(centerX,centerY,location):
    l=[]
    for x,y in location:    
        radius=np.sqrt((y-centerY)**2+(x-centerX)**2)
        l.append(radius)
    return l
        

@jit
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

t=image_location("daen.jpg",2)


##
# 初期値を書く
# 大きくして行く(rを)
#　どこかでぶつかるから,それをずらす.
# また大きくする
# 大きくしきれなければそれが解
##

#初期値
X=200
Y=100
R=70

#Rを大きくして行く
#Rとradiusが等しくなったら.
#ちょこっと動かす.



res=circle_checker(X,Y,t)








