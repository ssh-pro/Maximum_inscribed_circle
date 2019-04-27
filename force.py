#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 16:51:53 2019

@author: joil
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
import math
from numba.decorators import jit

@jit
def CircleFitting(x,y):
    sumx  = sum(x)
    sumy  = sum(y)
    sumx2 = sum([ix ** 2 for ix in x])
    sumy2 = sum([iy ** 2 for iy in y])
    sumxy = sum([ix * iy for (ix,iy) in zip(x,y)])

    F = np.array([[sumx2,sumxy,sumx],
                  [sumxy,sumy2,sumy],
                  [sumx,sumy,len(x)]])

    G = np.array([[-sum([ix ** 3 + ix*iy **2 for (ix,iy) in zip(x,y)])],
                  [-sum([ix ** 2 *iy + iy **3 for (ix,iy) in zip(x,y)])],
                  [-sum([ix ** 2 + iy **2 for (ix,iy) in zip(x,y)])]])

    T=np.linalg.inv(F).dot(G)

    cxe=float(T[0]/-2)
    cye=float(T[1]/-2)
    re=math.sqrt(cxe**2+cye**2-T[2])
    return cxe,cye,re

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

@jit
def circle_checker(centerX,centerY,x,y,rad):
    #被っていたら
    radius=np.sqrt((y-centerY)**2+(x-centerX)**2)
    if radius-rad<1:
        if radius-rad<-1:
        l=1
    else:
        l=0
    return l

ggg=image_location("daen.jpg",0)

#それぞれに,考えうる物が入っている.
lx=[]
ly=[]
lr=[]
#
#やり方.
#得られた結果を全部に試してみて,外に出ないかを確かめる
#とりあえず塗りつぶしてみる.
#その塗りつぶした座標に入って入ればおk
#入っていなければアウト
#入るRで最大を求める
#



#塗りつぶされたものにCircleを描画する.
#描画したものと描画されていないものを比べる
#全く同じ->円の中にある
#少しでも異なる->円の外にある



eee=[]

for var in range(0,len(lr)):
    aaa=cv2.imread("drack.jpeg",0)
    circle=cv2.circle(img=aaa, center=(lx[var],ly[var]), radius=lr[var], color=(255,0,0), thickness=1)
    if (circle == aaa).all() = True:
        eee.append(lx[var],ly[var],lr[var])
    else:
        pass












