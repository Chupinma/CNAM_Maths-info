from PIL import Image
import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt
from skimage import feature
import cv2 as cv

# Charger l'image en niveaux de gris
filepath = r"D:\01_Travail_Etudes\01_Ecoles\CNAM\M2_2026-2027\Maths-info\Filtre de Camy\image.jpg"
img = Image.open(filepath).convert("L")

# Convertir en matrice numpy
matrice = np.array(img)

img2 = cv.imread(filepath, cv.IMREAD_GRAYSCALE)
contours = cv.Canny(img2,100,200) #seuil mini de 100, maxi de 200

#contours = feature.canny(matrice, sigma=3)
#plt.imshow(contours,cmap='gray') #cmap = "gray" pour une gamme couleur en niveaux de gris

# Application du flou gaussien (mode 'same' pour même taille)
# boundary = "wrap" pour enroulement (bords)
gaussien = 1/163*np.array([[2,4,6,4,2],
                          [4,9,12,9,4],
                          [6,12,15,12,6],
                          [4,9,12,9,4],
                          [2,4,6,4,2]])
img_array_gaussien = convolve2d(matrice, gaussien, mode='same', boundary = 'wrap')

# Définir un noyeau de convolution (ex: détection de contours avec les opérateurs de Sobel)
kernelx = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])
kernely = np.array([[ 1, 2, 1],
                    [ 0, 0, 0],
                    [-1,-2,-1]])

# Appliquer les convolutions pour calcul du gradient
conv1 = convolve2d(matrice, kernelx, mode='same', boundary='fill', fillvalue=0)
conv2 = convolve2d(matrice, kernely, mode='same', boundary='fill', fillvalue=0)

# Calcul de la norme du gradient
norm_grad = np.sqrt(np.power(conv1,2)+np.power(conv2,2))

# Afficher l'image originale
plt.figure(figsize=(18, 10)) #taille de la figure : largeur 18 et hauteur 10
plt.subplot(2, 2, 1) #2 lignes, 1 colonne, 1er plot
plt.title("Image originale")
plt.imshow(matrice, cmap='gray') #cmap = "gray" pour une gamme couleur en niveaux de gris
plt.axis('off')

# Afficher l'image après le flou gaussien
plt.subplot(2, 2, 2) #2 lignes, 1 colonne, 2ème plot
plt.title("Image après flou gaussien")
plt.imshow(img_array_gaussien, cmap='gray') 
plt.axis('off')

# Afficher la norme du gradient
plt.subplot(2, 2, 3) #2 lignes, 2 colonnes, 3ème plot
plt.title("Norme du Gradient")
plt.imshow(norm_grad, cmap='gray')
plt.axis('off')

# Afficher après hystérésis
plt.subplot(2, 2, 4) #2 lignes, 2 colonnes, 4ème plot
plt.title("après hystérésis")
plt.imshow(contours,cmap='gray') 
plt.axis('off')

plt.show()