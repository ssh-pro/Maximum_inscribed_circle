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
    ret, thresh = cv2.threshold(imgray, 0, 255, 0)
    #ret, thresh = cv2.threshold(a, 1, 255, 0)
    contours = cv2.findContours((thresh), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[1]
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
    try:    
        l.append(imgpath)
        l.append([x,w,y,h])
        cv2.imwrite(exitpath,target)
    except:
        pass
    return l

@jit
def image_location(img):
    res=[]
    for y in range(0,np.shape(img)[0]):
        for x in range(0,np.shape(img)[1]):
            a=[]
            color=img[y][x]
            b=color[0]
            if b != 255:
                a.append(x)
                a.append(y)
                res.append(a)
            else:
                pass
    return res

def wa(comp,exdir1,size):
    path=comp     
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
    cv2.imwrite(exdir1,im)


def mover(location_list,center_x,center_y,radius):
    if len(location_list)<2:
        touch_x=location[0][0]
        touch_y=location[0][1]
        
        #中心からの差を求める
        if center_x < touch_x:
            move_x=touch_x-center_x
        else:
            move_x=center_x-touch_x
            
        if center_y < touch_y:
            move_y=touch_y-center_y
        else:
            move_y=center_y-touch_y
        
        
        #動かす方向を決める 真上=0 時計回り
        if move_y+move_x==radius:
            if gy>0:    
                theta=0
            else:
                theta=270

        if move_y+move_x==-radius:
            if gy<0:    
                theta=90
            else:
                theta=180            
        
        #45度は,比率が大体1:1+sqrt(2)くらいになる
    
    else:
        #複数の点で接する場合.
        #二重ループになってしまうため,最適な手法を考えて欲しい.
        

        #最も遠い二点
        w1=[wx1,wy1]
        w2=[wx2,wy2]
        if wx1 < wx2:
            move_x=wx2-wx1
        else:
            move_x=wx1-wx2
            
        if wy1 < wy2:
            move_y=wy2-wy1
        else:
            move_y=wy1-wy2      
        
        #最も遠い点を結ぶ線分とその線分の垂直二等分線の交点をHとすると,
        H=[wx1+move_x,wy1+move_y]
        #のように書くことができる.(x,yの正負によって変化する)
        #Hがわかると,上のif文のように,一点で交わる場合と同じである.

def circle_writer(img_hig,img_wid,cx,cy,r):
    img = np.ones((img_wid,img_hig),np.uint8)*255
    cv2.circle(img, (cx, cy), r, (0, 0, 0), thickness=1)
    return img
