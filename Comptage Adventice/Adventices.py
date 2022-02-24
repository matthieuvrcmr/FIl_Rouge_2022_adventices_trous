[# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 15:01:51 2022

@author: ludov
"""
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from skimage.filters import threshold_yen


# Calcul de la surface d'adventices en appliquant un filtre YEN et affiche la photo il faut renseigner le chemin vers l'image
def surface_adventices_yen(img_path):
    rgb_image = cv.imread(img_path)
    green_channel = rgb_image[:,:,1]
    yen_th = threshold_yen(green_channel)
    ret1,th1 = cv.threshold(green_channel,yen_th,255,cv.THRESH_BINARY)
    plt.imshow(th1)
    plt.show()
    return th1, 100*np.sum(th1==0)/th1.size

# Calcul de la surface d'adventices en appliquant un filtre OTSU et affiche la photo il faut renseigner le chemin vers l'image
def surface_adventices_otsu(img_path):
    rgb_image = cv.imread(img_path)
    green_channel = rgb_image[:,:,1]
    ret2,th2 = cv.threshold(green_channel,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)   
    plt.imshow(th2)
    plt.show()
    return th2, 100*np.sum(th2==0)/th2.size

    
    

"""Renseigner le chemin vers les images, ici on utilise les images DJI_0050 à DJI_0060"""
PATH = "photos_crop/"
IMG_NAMES = ["DJI_00"+str(nb)+"_crop.JPG" for nb in np.arange(50,61)]
    
# Auto Thresold Yen
for IMG_NAME in IMG_NAMES:
    th, surf_adv = surface_adventices_yen(IMG_NAME)
    cv.imwrite(PATH+IMG_NAME[:13]+"_yen.JPG", th)
    print(IMG_NAME+" -> surface de "+str(round(surf_adv,2))+" % d'adventices.")

# Auto Thresold Otsu
for IMG_NAME in IMG_NAMES:
    th, surf_adv = surface_adventices_otsu(IMG_NAME)
    cv.imwrite(PATH+IMG_NAME[:13]+"_otsu.JPG", th)
    print(IMG_NAME+" -> surface de "+str(round(surf_adv,2))+" % d'adventices.")

#affichage des photos
rgb_image = cv.imread("photos_crop/DJI_0057_crop.JPG")
green_channel = rgb_image[:,:,1]
yen_th = threshold_yen(green_channel)
ret1,th1 = cv.threshold(green_channel,yen_th,255,cv.THRESH_BINARY)
ret2,th2 = cv.threshold(green_channel,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
fig = plt.figure(figsize=(10, 7))
fig.add_subplot(1,2,1)
plt.imshow(th1)
plt.title('DJI_0057 : filtre Yen sur canal vert')
fig.add_subplot(1,2,2)
plt.imshow(th2)
plt.title('DJI_0057 : filtre Otsu sur canal vert')
plt.savefig('Adventices_Filtre_Yen_Otsu')



