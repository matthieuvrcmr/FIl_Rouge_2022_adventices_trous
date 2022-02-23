# -*- coding: utf-8 -*-
"""
Fonctions:
    (1) encardrer les trous à partir de l'image originale et les annotations en format csv
    (2) decouper les imagette à partir de l'image originale et les annotations en format csv

Arg à entrer:
    (1) ligne 83: chemin de l'image: image_path 
    (2) ligne 84: chemin du fichier d'annotations en format csv: csv_path

@author: Kexin
"""
#--------------------------
# import
#--------------------------
import cv2
import os
import matplotlib.pyplot as plt

cwd = os.getcwd()
print(cwd)

#--------------------------
# fonctions
#--------------------------

def show_annotation(image_path, csv_path):
    """
    Args:
        image_path: le chemin de l'image
        csv_path: le chemin du file en format csv avec les coordonnées des annotations
    Output:
        l'image annoté avec des encadrés rouges, renommé en "nom d'origine + trou", dans le meme dossier avec les images originales
    """
    img = cv2.imread(image_path)
    annotations = open(csv_path, encoding='utf-8')
    for line in annotations:
        ls = line.split(',')
        img = cv2.rectangle(img, (int(ls[1]), int(ls[2])), (int(ls[1])+int(ls[3]), int(ls[2])+int(ls[4])), (0, 0, 255), 2) # encadrer en line rouge, taill = 2
    extension = os.path.splitext(image_path)[1]
    image_path_without_ext = os.path.splitext(image_path)[0]
    plt.imshow(img)
    cv2.imwrite(image_path_without_ext+'_trou'+ extension, img)
    
    return


def decouper_annotation(image_path, csv_path):
    """
    Args:
        image_path: le chemin de l'image
        csv_path: le chemin du file en format csv avec les coordonnées des annotations
    Output:
        les imagettes dans le dossier portant le même nom que l'image
    """
    nom_img = os.path.splitext(os.path.basename(image_path))[0] # pour avoir le nom de l'image
    # print(nom_img)
    dossier_path = os.path.join(os.path.dirname(image_path), nom_img)
    if not os.path.exists(dossier_path):
        os.makedirs(dossier_path) # créez un dossier portant le même nom que l'image dans le dossier où se trouve l'image


    extension = os.path.splitext(image_path)[1]
    img = cv2.imread(image_path)
    annotations = open(csv_path, encoding='utf-8')
    i=0
    for line in annotations:
        i+=1
        ls = line.split(',')
        if ls[3] != '0' and ls[4] != '0':
            imagette = img[int(ls[2]):int(ls[2])+int(ls[4]), int(ls[1]):int(ls[1])+int(ls[3])]
            imagette_path = os.path.join(dossier_path, nom_img+'_'+str(i)+extension)
            cv2.imwrite(imagette_path, imagette)

    return



#--------------------------
# main
#--------------------------

"""
les chemins à remplir
"""

image_path = 'DJI_0012.JPG'
csv_path = 'DJI_0012.csv'

show_annotation(image_path, csv_path)
decouper_annotation(image_path, csv_path)
