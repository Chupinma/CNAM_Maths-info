from PIL import Image
import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt
import cv2 as cv

# 1. Charger l'image en niveaux de gris
filepath = r"D:\01_Travail_Etudes\01_Ecoles\CNAM\M2_2026-2027\Maths-info\CNAM_Maths-info\TD - Filtre de Canny\dessin.jpg"
img = Image.open(filepath).convert("L") # "L" = grayscale

img2 = cv.imread(filepath, cv.IMREAD_GRAYSCALE)
contours = cv.Canny(img2,100,200) #seuil mini de 100, seuil maxi de 200


# 2. Convertir en matrice numpy
img_array = np.array(img)

# 3. Application du flou gaussien (mode 'same' pour même taille)
# boundary = "wrap" pour enroulement (bords)
gaussien = 1/163 * np.array([[2, 4, 6, 4, 2],
                             [4, 9,12, 9, 4],
                             [6,12,15,12, 6],
                             [4, 9,12, 9, 4],
                             [2, 4, 6, 4, 2]])
img_array_gaussien = convolve2d(img_array , gaussien, mode='same', boundary='wrap')

# 4. Définir un noyau de convolution (ex: détection de contours avec les opérateurs de Sobel)
kernelx = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])
kernely = np.array([[ 1, 2, 1],
                    [ 0, 0, 0],
                    [-1,-2,-1]])

# 5. Appliquer les convolutions pour calcul du gradient
conv1 = convolve2d(img_array, kernelx, mode='same', boundary='fill', fillvalue=0)
conv2 = convolve2d(img_array, kernely, mode='same', boundary='fill', fillvalue=0)

# 6. Calcul de la norme du gradient
norm_grad = np.sqrt(np.power(conv1,2)+np.power(conv2,2))

# 7. Afficher l'image originale
plt.figure(figsize=(18, 10))
plt.subplot(2, 2, 1) #2 lignes, 2 colonnes, 1er plot
plt.title("Image originale")
plt.imshow(img_array, cmap='gray')
plt.axis('off') # pas d'axes sur le graphique

# 8. Afficher l'image après le flou gaussien
plt.subplot(2, 2, 2) #2 lignes, 2 colonnes, 2ème plot
plt.title("Image après flou gaussien")
plt.imshow(img_array_gaussien, cmap='gray')
plt.axis('off')

# 9. Afficher la norme du gradient
plt.subplot(2, 2, 3) #2 lignes, 2 colonnes, 3ème plot
plt.title("Norme du Gradient")
plt.imshow(norm_grad, cmap='gray')
plt.axis('off')

# 10. Afficher après hystérésis
plt.subplot(2, 2, 4) #2 lignes, 2 colonnes, 4ème plot
plt.title("Après hystérésis")
plt.imshow(contours, cmap = 'gray') #cmap = "gray" pour une gamme couleur en niveaux de gris
plt.axis('off')

plt.show()