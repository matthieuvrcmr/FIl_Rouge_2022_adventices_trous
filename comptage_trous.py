#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 14:57:35 2022

@author: matthieuvercaemer
"""

""""Créer un dossier général et y placer les dossiers de sortie du programme de kexin 'trou_decouper01'
Ne déposer que les dossiers avec les imagettes dans ce dossier général"""

import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
from skimage.filters import threshold_yen


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
"""estimation des erreurs dans le comptage des trous, pour chaque image on a sélectionné
au hasard 10% des imagettes et on compare le comptage manuel avec le comptage auto"""

DJI_0003_selec = ['DJI_0003_70.JPG', 'DJI_0003_35.JPG', 'DJI_0003_81.JPG',
       'DJI_0003_52.JPG', 'DJI_0003_24.JPG', 'DJI_0003_58.JPG',
       'DJI_0003_71.JPG', 'DJI_0003_7.JPG', 'DJI_0003_50.JPG']

DJI_0004_selec = ['DJI_0004_19.jpg', 'DJI_0004_55.jpg', 'DJI_0004_93.jpg',
       'DJI_0004_40.jpg', 'DJI_0004_77.jpg', 'DJI_0004_106.jpg',
       'DJI_0004_27.jpg', 'DJI_0004_57.jpg', 'DJI_0004_129.jpg',
       'DJI_0004_100.jpg', 'DJI_0004_76.jpg', 'DJI_0004_51.jpg',
       'DJI_0004_21.jpg']

DJI_0005_selec = ['DJI_0005_117.jpg', 'DJI_0005_90.jpg', 'DJI_0005_11.jpg',
       'DJI_0005_190.jpg', 'DJI_0005_143.jpg', 'DJI_0005_85.jpg',
       'DJI_0005_30.jpg', 'DJI_0005_99.jpg', 'DJI_0005_169.jpg',
       'DJI_0005_202.jpg', 'DJI_0005_194.jpg', 'DJI_0005_112.jpg',
       'DJI_0005_137.jpg', 'DJI_0005_30.jpg', 'DJI_0005_126.jpg',
       'DJI_0005_114.jpg', 'DJI_0005_134.jpg', 'DJI_0005_98.jpg',
       'DJI_0005_193.jpg', 'DJI_0005_74.jpg', 'DJI_0005_28.jpg']

DJI_0008_selec = ['DJI_0008_123.jpg', 'DJI_0008_48.jpg', 'DJI_0008_100.jpg',
       'DJI_0008_6.jpg', 'DJI_0008_51.jpg', 'DJI_0008_60.jpg',
       'DJI_0008_75.jpg', 'DJI_0008_27.jpg', 'DJI_0008_93.jpg',
       'DJI_0008_11.jpg', 'DJI_0008_76.jpg', 'DJI_0008_52.jpg',
       'DJI_0008_21.jpg']

DJI_0009_selec = ['DJI_0009_61.jpg', 'DJI_0009_40.jpg', 'DJI_0009_93.jpg',
       'DJI_0009_68.jpg', 'DJI_0009_19.jpg', 'DJI_0009_20.jpg',
       'DJI_0009_66.jpg', 'DJI_0009_96.jpg', 'DJI_0009_69.jpg',
       'DJI_0009_5.jpg']

DJI_0010_selec = ['DJI_0010_85.jpg', 'DJI_0010_62.jpg', 'DJI_0010_93.jpg',
       'DJI_0010_1.jpg', 'DJI_0010_39.jpg', 'DJI_0010_104.jpg',
       'DJI_0010_84.jpg', 'DJI_0010_28.jpg', 'DJI_0010_105.jpg',
       'DJI_0010_86.jpg', 'DJI_0010_32.jpg']

DJI_0011_selec =['DJI_0011_59.jpg', 'DJI_0011_106.jpg', 'DJI_0011_28.jpg',
       'DJI_0011_34.jpg', 'DJI_0011_36.jpg', 'DJI_0011_74.jpg',
       'DJI_0011_43.jpg', 'DJI_0011_75.jpg', 'DJI_0011_8.jpg',
       'DJI_0011_107.jpg', 'DJI_0011_71.jpg']

DJI_0012_selec = ['DJI_0012_18.JPG', 'DJI_0012_1.JPG', 'DJI_0012_21.JPG',
       'DJI_0012_14.JPG', 'DJI_0012_66.JPG', 'DJI_0012_50.JPG',
       'DJI_0012_34.JPG', 'DJI_0012_85.JPG', 'DJI_0012_67.JPG']


def comptage_imagettes(liste_imagettes):
    """"Prend en entrée une des listes d'imagettes ci dessus et renvoie le nombre de trous
    comptés dans chaque imagette de la liste"""
    for imagette in liste_imagettes:
        PATH = GEN_DIRECTORY+imagette[:8]+"/"+imagette
        nb_trous = comptage_trous(PATH)
        print("Il y a "+str(nb_trous)+" dans l'imagette "+imagette)
        
#comptage_imagettes(DJI_0003_selec)
#comptage_imagettes(DJI_0004_selec)
#comptage_imagettes(DJI_0005_selec)
#comptage_imagettes(DJI_0008_selec)
#comptage_imagettes(DJI_0009_selec)
#comptage_imagettes(DJI_0010_selec)
#comptage_imagettes(DJI_0011_selec)
#comptage_imagettes(DJI_0012_selec)