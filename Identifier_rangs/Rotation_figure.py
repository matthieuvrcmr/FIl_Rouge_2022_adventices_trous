from scipy import ndimage
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Effectue une rotation de l'image en complétant les coins par des pixels noirs (0)
def rotate_figure(some_digit,angle):
    some_digit_rotated = ndimage.rotate(some_digit,angle,reshape=True)
    return(some_digit_rotated)

# Calcule un score moyen sur chaque ligne de l'image
def score_image(image,score):
    s = 0
    nlignes = len(image)
    for k in range(nlignes):
        ligne = np.array(image[k])
        ligne_pos = ligne>0
        if sum(ligne_pos) > 0:
            if score == "minmax":
                ind_ligne = max(ligne[ligne_pos]) - min(ligne[ligne_pos])
            if score == "var":
                ind_ligne = np.var(ligne[ligne_pos])
        else:
            ind_ligne = 0
        s += ind_ligne
    return s/nlignes

# Pour différentes inclinaisons, on calcule le score correspondant pour l'image obtenue

def score_rotation(image,list_angle,score):
    list_scores = []
    for angle in list_angle:
        print(angle)
        list_scores += [score_image(rotate_figure(image,angle),score)]
    return list_scores

#img_tmp = cv2.imread("maize\drone_2021_06-06\DJI_0065.JPG",0)
img_tmp = cv2.imread("maize\drone_2021_06-06\DJI_0014.JPG",0)
plt.imshow(img_tmp)
plt.show()

ANGLES = np.array([89,89.3,89.5,89.6,89.8,90,90.3])

list_scores = score_rotation(img_tmp,ANGLES,score="var")

plt.plot(ANGLES-90,list_scores)
plt.xlabel("Angle de rotation")
plt.ylabel("Score Moyen")
plt.title("Evolution de la variance moyenne \n DJI_0014")
plt.savefig("Rotation_var")
plt.show()

"""
list_scores = score_rotation(img_tmp,ANGLES,score="minmax")

plt.plot(ANGLES,list_scores)
plt.xlabel("Angle de rotation")
plt.ylabel("Score Moyen")
plt.title("Evolution du score max-min moyen \n DJI_0014")
plt.savefig("Rotation_minmax")
plt.show()
"""

## Rotation de l'image selon le critère de la variance
cv2.imwrite("Rotation_-0.4_degre.png",rotate_figure(img_tmp,-0.4))

## rotation de l'image selon le crière du max-min
#cv2.imwrite("Rotation_3_degre.png",rotate_figure(img_tmp,3))



### Facteur de Circularité
### Définit comme f = 4 pi aire/perimetre**2.
### Plus f proche de 1, plus la forme se rapproche d'un cercle




