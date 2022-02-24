#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 14:57:35 2022

@author: matthieuvercaemer
"""


import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
from skimage.filters import threshold_yen


""""Créer un dossier général et y placer les dossiers de sortie du programme de 'trou_decouper01'
Ne déposer que les dossiers avec les imagettes dans ce dossier général"""

"""Renseigner ci-dessous le chemin vers le dossier général"""
GEN_DIRECTORY = "/Users/matthieuvercaemer/Desktop/IODAA/IODAA/Fil_rouge/Comptage_trous/Imagettes/" #renseigner le chemin vers le dossier contenant les dossiers avec les imagettes


def comptage_trous(path_to_img):
    "Compte le nombre de trous dans l'image dont on a renseigné le chemin"
    image = cv2.imread(path_to_img)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    ret,th = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_TRIANGLE)
    kernal = np.ones((2, 2), np.uint8)
    erosion = cv2.erode(th,kernal)
    contours, hierarchy = cv2.findContours(erosion, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    objects = len(contours)
    #fig = plt.figure(figsize=(10, 7))
    #fig.add_subplot(1,2,1)
    #plt.imshow(image)
    #plt.title('Photo originale')
    #fig.add_subplot(1,2,2)
    #plt.imshow(erosion)
    #plt.title('Filtre triangle:'+str(objects)+'trous détectés')
    return(objects)
    
#print(comptage_trous('Comptage_trous/Imagettes/DJI_0004/DJI_0004_12.jpg'))


DIRECTORIES = os.listdir(GEN_DIRECTORY) #obtient la liste de tous les dossiers contenant les imagettes
DIRECTORIES.remove('.DS_Store')
for directory in DIRECTORIES : #on rentre dans un dossier
    FILES = os.listdir(GEN_DIRECTORY+directory) #liste contenant toutes les imagettes du dossier
    nb_trous = 0
    for file in FILES :
        nb_trous += comptage_trous(GEN_DIRECTORY+directory+'/'+file)
    print('Il y a '+str(nb_trous)+' trous dans la photo '+directory)
    
    
##########################################################################
