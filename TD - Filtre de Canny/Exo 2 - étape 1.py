import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from scipy.signal import convolve2d

from scipy.ndimage import gaussian_filter

# Charger l'image
filepath = r"D:\01_Travail_Etudes\01_Ecoles\CNAM\M2_2026-2027\Maths-info\CNAM_Maths-info\TD - Filtre de Canny\image.jpg"
img = Image.open(filepath)

# Convertir en matrice numpy
img_array = np.array(img)
taille = img_array.shape
Hauteur = taille[0]
Largeur = taille[1]

""" # Matrice de zéros
M = np.zeros((Hauteur, Largeur), dtype=int)

# 3. Calculer les niveaux de gris
R = img_array[:, :, 0]
V = img_array[:, :, 1]
B = img_array[:, :, 2]

M = 0.299 * R + 0.587 * V + 0.114 * B """

img_array_copie = img_array
img_array_copie = gaussian_filter(img_array_copie,sigma = 1.4)

img_array_copie_ecart_05 = img_array
img_array_copie_ecart_2 = img_array
img_array_copie_ecart_05 = gaussian_filter(img_array_copie_ecart_05,sigma = 0.5)
img_array_copie_ecart_2 = gaussian_filter(img_array_copie_ecart_2,sigma = 2)
#gaussian_filter(img_array_copie,sigma = 1.4)


# 7. Afficher l'image originale
plt.figure(figsize=(18, 10))
plt.subplot(2, 3, 1) #2 lignes, 3 colonnes, 1er plot
plt.title("Image RGB")
plt.imshow(img_array)
plt.axis('off') # pas d'axes sur le graphique

""" # 8. Afficher l'image après le passage en grey scale
plt.subplot(2, 2, 2) #2 lignes, 2 colonnes, 2ème plot
plt.title("Image Grey scale")
plt.imshow(M, cmap='gray')
plt.axis('off') """

# 8. Afficher l'image après le flou gaussien
plt.subplot(2, 3, 4) #2 lignes, 2 colonnes, 2ème plot
plt.title("Image après le flou gaussien")
plt.imshow(img_array_copie_ecart_05)
plt.axis('off')

# 8. Afficher l'image après le flou gaussien
plt.subplot(2, 3, 5) #2 lignes, 2 colonnes, 2ème plot
plt.title("Image après le flou gaussien")
plt.imshow(img_array_copie)
plt.axis('off')

# 8. Afficher l'image après le flou gaussien
plt.subplot(2, 3, 6) #2 lignes, 2 colonnes, 2ème plot
plt.title("Image après le flou gaussien")
plt.imshow(img_array_copie_ecart_2)
plt.axis('off')

plt.show()