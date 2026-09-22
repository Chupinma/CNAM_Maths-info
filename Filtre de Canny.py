from PIL import Image
import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt
from skimage import feature
import cv2 as cv

# Charger l'image en niveaux de gris
##img = Image.open("image.jpg").convert("L")

# Convertir en matrice numpy
#matrice = np.array(img)
filepath = r"D:\01_Travail_Etudes\01_Ecoles\CNAM\M2_2026-2027\Maths-info\Filtre de Camy\image.jpg"
img = cv.imread(filepath, cv.IMREAD_GRAYSCALE)
contours = cv.Canny(img,100,200) #seuil mini de 100, maxi de 200

#contours = feature.canny(matrice, sigma=3)
plt.imshow(contours,cmap='gray') #cmap = "gray" pour une gamme couleur en niveaux de gris

plt.show()