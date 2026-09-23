import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Charger l'image
filepath = r"D:\01_Travail_Etudes\01_Ecoles\CNAM\M2_2026-2027\Maths-info\CNAM_Maths-info\TD - Filtre de Canny\image.jpg"
img = Image.open(filepath)

# Convertir en matrice numpy
img_array = np.array(img)
taille = img_array.shape
Hauteur = taille[0]
Largeur = taille[1]

# Matrice de zéros
M = np.zeros((Hauteur, Largeur), dtype=int)

# 3. Calculer les niveaux de gris
R = img_array[:, :, 0]
V = img_array[:, :, 1]
B = img_array[:, :, 2]

M = 0.299 * R + 0.587 * V + 0.114 * B

# 7. Afficher l'image originale
plt.figure(figsize=(18, 10))
plt.subplot(2, 2, 1) #2 lignes, 2 colonnes, 1er plot
plt.title("Image RGB")
plt.imshow(img_array, cmap='gray')
plt.axis('off') # pas d'axes sur le graphique

# 8. Afficher l'image après le flou gaussien
plt.subplot(2, 2, 2) #2 lignes, 2 colonnes, 2ème plot
plt.title("Image Grey scale")
plt.imshow(M, cmap='gray')
plt.axis('off')

plt.show()