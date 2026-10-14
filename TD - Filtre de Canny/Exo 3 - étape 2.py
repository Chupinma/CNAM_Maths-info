import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from scipy.signal import convolve2d

# Charger l'image
filepath = r"D:\01_Travail_Etudes\01_Ecoles\CNAM\M2_2026-2027\Maths-info\CNAM_Maths-info\TD - Filtre de Canny\image.jpg"
img = Image.open(filepath).convert("L")

# Convertir en matrice numpy
img_array = np.array(img)
taille = img_array.shape

img_array_copie = img_array
img_array_copie = gaussian_filter(img_array_copie,sigma = 1.4)

# Définir un noyau de convolution (ex: détection de contours avec les opérateurs de Sobel)
kernelx = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])
kernely = np.array([[ 1, 2, 1],
                    [ 0, 0, 0],
                    [-1,-2,-1]])

# 5. Appliquer les convolutions pour calcul du gradient
conv1 = convolve2d(img_array_copie, kernelx, mode='same', boundary='fill', fillvalue=0)
conv2 = convolve2d(img_array_copie, kernely, mode='same', boundary='fill', fillvalue=0)

# Valeur absolue de ces gradients
conv1 = np.abs(conv1)
conv2 = np.abs(conv2)

# 6. Calcul de la norme du gradient
norm_grad = np.sqrt(np.power(conv1,2)+np.power(conv2,2))

#  Afficher la valeur abs des gradients
plt.figure(figsize=(18, 10))
plt.subplot(2, 3, 1) #2 lignes, 2 colonnes, 1er plot
plt.title("Image originale")
plt.imshow(img_array, cmap='gray')
plt.axis('off') # pas d'axes sur le graphique

plt.subplot(2, 3, 4)
plt.title("Val abs gradient en x")
plt.imshow(conv1, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.title("Val abs gradient en y")
plt.imshow(conv2, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 6) 
plt.title("norme du gradient")
plt.imshow(norm_grad, cmap='gray')
plt.axis('off')

plt.show()