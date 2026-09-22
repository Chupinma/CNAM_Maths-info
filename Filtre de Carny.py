from PIL import Image
import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt

img = Image.open(r"D:\01_Travail_Etudes\01_Ecoles\CNAM\M2_2026-2027\Maths-info\Filtre de Camy\image.jpg").convert("L")
matrice = np.array(img)

gaussien = 1/163*np.array([[2,4,6,4,2],
                          [4,9,12,9,4],
                          [6,12,15,12,6],
                          [4,9,12,9,4],
                          [2,4,6,4,2]])
img_array_gaussien = convolve2d(matrice, gaussien, mode='same', boundary = 'wrap')

# 4. Afficher l'image originale
plt.figure(figsize=(18, 10)) #taille de la figure : largeur 18 et hauteur 10
plt.subplot(2, 1, 1) #2 lignes, 1 colonne, 1er plot
plt.title("Image originale")
plt.imshow(matrice, cmap='gray') #cmap = "gray" pour une gamme couleur en niveaux de gris
plt.axis('off')

# 5. Afficher l'image après le flou gaussien
plt.subplot(2, 1, 2) #2 lignes, 1 colonne, 2ème plot
plt.title("Image après flou gaussien")
plt.imshow(img_array_gaussien, cmap='gray') 
plt.axis('off')

plt.show()

##print(matrice)
##print(matrice.shape)
##(800,1200)
#img.show()