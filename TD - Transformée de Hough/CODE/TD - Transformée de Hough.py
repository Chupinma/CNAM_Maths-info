# Librairies
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2 as cv

# Charger l'image en niveaux de gris
filepath = r"D:\01_Travail_Etudes\01_Ecoles\CNAM\M2_2026-2027\Maths-info\Filtre de Camy\image.jpg"
#img = Image.open(filepath).convert("L")

img2 = cv.imread(filepath, cv.IMREAD_GRAYSCALE)
contours = cv.Canny(img2,100,200) #seuil mini de 100, seuil maxi de 200

# Convertir en matrice numpy
matrice = np.array(contours)
taille = matrice.shape
Hauteur = taille[0]
Largeur = taille[1]

# Initialiser M comme tableau à deux dimensions (0 à 180, -rho_max à rho_max) avec des zéros
rho_max = int(np.sqrt(Hauteur**2 + Largeur**2))
M = np.zeros((180, int(2 * rho_max+1)), dtype=int)

# Récupérer les coordonnées des pixels
y, x = np.nonzero(contours)

for x,y in zip(x,y) :
    for theta in range(0, 180):
        theta_rad = np.deg2rad (theta)
        rho = x*np.cos(theta_rad) + y*np.sin(theta_rad)
        rho = round(rho)
        rho_index = rho + rho_max
        M[theta,rho_index]=M[theta,rho_index]+1

seuil_min = 100
theta, rho_index = np.where(M > seuil_min)
rho = rho_index - rho_max

M2 = np.column_stack((theta, rho))

print (M2)

'''for t, r in zip(theta, rho):
    print("theta =", t, "rho =", r)
    '''
