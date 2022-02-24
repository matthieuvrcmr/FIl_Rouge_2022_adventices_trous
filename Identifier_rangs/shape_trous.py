#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 11:10:14 2022

@author: matthieuvercaemer
"""

"""
@author: Kexin

pour distinger les trous de corbeaux des traces de tracteurs par méthodes:
    (1) HoughCircles
    (2) circularité + area
    (3) circularité
    (4) area

remplir 'path_to_img' dans Main

Output:
    1. generer un image avec les tous détectés encadreé en circle verte pour les quatre méthodes
    2. le nombre de trous détectés par chaque méthode 

"""
import cv2
import os
import matplotlib.pyplot as plt
import numpy as np
from skimage.filters import threshold_yen
import math
# import shutil
# import pdb


################################################################################

'Hough Circles'

def identifier_rond_par_HoughCircles(path_to_img, dp=1, minDist=5, param1=100, param2=8, minRadius=1, maxRadius=5):
    """
    Méthodes HoughCircles pour trouver les formes rondes 
    Arg:
        path_to_img :
        argumente de cv2.HoughCircles à jouer
    Output:
        cv2.imwrite(image_path_without_ext+'_HoughCircles'+ extension, image)
    Return:
        len(circles[0]) = nombre de circle trouver
    """
    image = cv2.imread(path_to_img)
    extension = os.path.splitext(path_to_img)[1]
    image_path_without_ext = os.path.splitext(path_to_img)[0]
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=dp, minDist=minDist, param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)
    """
    cv2.HoughCircles: Finds circles in a grayscale image using the Hough transform.
    elle prend l'image 8-bit, single-channel, grayscale input image.

    methode: #HOUGH_GRADIENT and #HOUGH_GRADIENT_ALT
    l'explication ci-dessous est pour #HOUGH_GRADIENT
    dp: 
        Inverse ratio of the accumulator resolution to the image resolution. 
        图像大小(分辨率)操作???? 
        dp=1 , the accumulator(累加器, 指啥???) has the same resolution as the input image. 
        If dp=2 , the accumulator has half as big width and height. 
        For #HOUGH_GRADIENT_ALT the recommended value is dp=1.5, unless some small very circles need to be detected.
    minDist: 
        Minimum distance between the centers of the detected circles. (注意是圆心距离)
        它表示传递给canny边缘检测算子的高阈值,而低阈值为高阈值的一半
    param1: 
        the higher threshold of the two passed to the Canny edge detector (the lower one is twice smaller). 
    param2: 
        the accumulator threshold for the circle centers at the detection stage. 
        The smaller it is, the more false circles may be detected. 
        Circles, corresponding to the larger accumulator values, will be returned first. 
        表示在检测阶段圆心的累加器阈值,它越小,就越可以检测到更多根本不存在的圆,而它越大的话,能通过检测的圆就更加接近完美的圆形了
    minRadius: 
        Minimum circle radius.
    maxRadius: 
        Maximum circle radius. 
        If <= 0, uses the maximum image dimension. 
        If < 0, #HOUGH_GRADIENT returns centers without finding the radius. 
    """

    for c in circles[0]:
        x = int(c[0])
        y = int(c[1])
        r = int(c[2])
        # x = round(c[0])
        # y = round(c[1])
        # r = round(c[2])

        image = cv2.circle(image,(x,y),r,(0,255,0),1)
    
    cv2.imwrite(image_path_without_ext+'_HoughCircles'+ extension, image)
    
    # plt.imshow(image)
    # plt.show()
    return len(circles[0])


################################################################################

'Circularité + Aire'

def distinguer_trous_circularite_area(path_to_img, circularite_min=0.5, area_min=10, area_max=30):
    image = cv2.imread(path_to_img)
    extension = os.path.splitext(path_to_img)[1]
    image_path_without_ext = os.path.splitext(path_to_img)[0]

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    # cv2.imwrite(image_path_without_ext+'_Circularité_gray'+ extension,gray)
 
    ret,th = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_TRIANGLE)
    kernal = np.ones((2, 2), np.uint8)

    th=255-th # inverser la couleur, car cv2.HoughCircles detecte les pixels blanc
    cv2.imwrite(image_path_without_ext+'_Circularité_binaire'+ extension,th)

    # dilate_img = cv2.dilate(th, kernal, iterations=iteration_erosion_dilate)
    # erosion_img = cv2.erode(dilate_img, kernal, iterations=iteration_erosion_dilate)
    # cv2.imwrite('th_02.jpeg', erosion_img)

    contours, hierarchy = cv2.findContours(th, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(image,contours,-1,(0,0,255),1)
    # cv2.imwrite('test.jpeg', image)
    areas = []
    perimeters = []
    circularites = []
    contours_trous = []

    for c in contours:
        area=cv2.contourArea(c)
        perimeter=cv2.arcLength(c,True)

        if perimeter != 0:
            circularite = 4*math.pi*area/perimeter**2
            # circularites.append(circularite)

            if  circularite > circularite_min and area > area_min and area < area_max:
                contours_trous.append(c)

    image = cv2.imread(path_to_img)
    cv2.drawContours(image,contours_trous,-1,(0,255,0),1)
    cv2.imwrite(image_path_without_ext+'_Circularité_area'+ extension,image)

    return len(contours_trous)

################################################################################

'Circularité'

def distinguer_trous_circularite(path_to_img, circularite_min=0.5):
    image = cv2.imread(path_to_img)
    extension = os.path.splitext(path_to_img)[1]
    image_path_without_ext = os.path.splitext(path_to_img)[0]

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
 
    ret,th = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_TRIANGLE)
    kernal = np.ones((2, 2), np.uint8)

    th=255-th # inverser la couleur, car cv2.HoughCircles detecte les pixels blanc
    # cv2.imwrite(image_path_without_ext+'_Circularité_binaire'+ extension,th)
 
    contours, hierarchy = cv2.findContours(th, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours_trous = []

    for c in contours:
        area=cv2.contourArea(c)
        perimeter=cv2.arcLength(c,True)
        
        if perimeter != 0:
            circularite = 4*math.pi*area/perimeter**2
            if  circularite > circularite_min:
                contours_trous.append(c)
           
    image = cv2.imread(path_to_img)
    cv2.drawContours(image,contours_trous,-1,(0,255,0),1)
    cv2.imwrite(image_path_without_ext+'_Circularité'+ extension,image)

    return len(contours_trous), contours_trous

################################################################################

'Aire'

def distinguer_trous_area(path_to_img, area_min=10, area_max=30):
    image = cv2.imread(path_to_img)
    extension = os.path.splitext(path_to_img)[1]
    image_path_without_ext = os.path.splitext(path_to_img)[0]

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
 
    ret,th = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_TRIANGLE)
    kernal = np.ones((2, 2), np.uint8)

    th=255-th # inverser la couleur, car cv2.HoughCircles detecte les pixels blanc
    cv2.imwrite(image_path_without_ext+'_Circularité_binaire'+ extension,th)
 
    contours, hierarchy = cv2.findContours(th, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours_trous = []

    for c in contours:
        area=cv2.contourArea(c)
        perimeter=cv2.arcLength(c,True)
        
        if perimeter != 0:
            circularite = 4*math.pi*area/perimeter**2
            if  area > area_min and area < area_max:
                contours_trous.append(c)
           
    image = cv2.imread(path_to_img)
    cv2.drawContours(image,contours_trous,-1,(0,255,0),1)
    cv2.imwrite(image_path_without_ext+'_area'+ extension,image)

    return len(contours_trous)

################################################################################

'MAIN'


path_to_img = '/Users/matthieuvercaemer/Desktop/IODAA/IODAA/Fil_rouge/Comptage_trous/DJI_0009_trou.jpg'

AREA_MIN = 10
AREA_MAX = 10000

nb_trous= identifier_rond_par_HoughCircles(path_to_img, dp=1, minDist=5, param1=100, param2=8, minRadius=1, maxRadius=5)  
# parametres de cv2.HoughCircles() selon votre choix
print('nb_trous de HougeTramsform : ',nb_trous)

nb_trous = distinguer_trous_circularite_area(path_to_img, circularite_min=0.5, area_min=AREA_MIN, area_max=AREA_MAX)  
print('circulatite + area :', nb_trous)

nb_trous, coord_contours = distinguer_trous_circularite(path_to_img, circularite_min=0.5)
print('circulatite :', nb_trous)

nb_trous = distinguer_trous_area(path_to_img, area_min=AREA_MIN, area_max=AREA_MAX)
print('area :', nb_trous)