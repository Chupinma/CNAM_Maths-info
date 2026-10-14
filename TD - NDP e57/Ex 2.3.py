from pye57 import E57
import numpy as np
import matplotlib.pyplot as plt

filepath = r"D:\01_Travail_Etudes\01_Ecoles\CNAM\M2_2026-2027\Maths-info\Cours\1.3 - Cours Fichier E57\E57\Ex2.e57"

with E57(filepath) as e57:

    Liste_X_tot = []
    Liste_Y_tot = []
    Liste_Z_tot = []

    for i in range(e57.scan_count):
        data = e57.read_scan(i, ignore_missing_fields=True)

        Liste_X_tot.extend(data["cartesianX"])
        Liste_Y_tot.extend(data["cartesianY"])
        Liste_Z_tot.extend(data["cartesianZ"])

#Transformer mes listes en tableaux numpy
Liste_X_tot = np.array(Liste_X_tot)
Liste_Y_tot = np.array(Liste_Y_tot)
Liste_Z_tot = np.array(Liste_Z_tot)

# Extraire les coordonnées du dictionnaire data extrait du nuage de points
# Filtrer les points selon l'altitude avec tolérance autour de z_target
z_target = 0
tolerance = 0.01
mask = np.abs(Liste_Z_tot - z_target) <= tolerance

# Extraire les coordonnées X,Y,Z des points sélectionnés (projection)
x_coupe = Liste_X_tot[mask]
y_coupe = Liste_Y_tot[mask]
z_coupe = Liste_Z_tot[mask]

# Afficher le nombre de points total et le nombre de points après application du filtre
Nb_points_avant_mask = len(Liste_Z_tot)
print(Nb_points_avant_mask)

Nb_points = len(z_coupe)
print(Nb_points)

# Créer un tableau numpy de zéros de taille (500, 800)
Largeur = 800
Hauteur = 500
img=np.zeros((Hauteur,Largeur),dtype=np.uint8)
# Pour avoir un tableau rempli de 255 -> fond blanc
# img=np.full((Hauteur,Largeur),255,dtype=np.uint8)

# Determiner les bornes de mon image
x_min = min(x_coupe)
x_max = max(x_coupe)

y_min = min(y_coupe)
y_max = max(y_coupe)

# Opération de normalisation pour passer de mon intervale en coordonnées à des indices dans mon tableau (image)
x_coupe_indexed = np.interp(x_coupe, [x_min, x_max], [0,Largeur-1])
y_coupe_indexed = np.interp(y_coupe, [y_min, y_max], [0,Hauteur-1])

# Passage des indices en entiers
x_int = x_coupe_indexed.astype(np.int32)
y_int = y_coupe_indexed.astype(np.int32)

# Parcourir tes points
for x, y in zip(x_int, y_int):
    img[y, x] = 255 # 0 si on à fait un fond blanc / +=1 si on veux + ou + d'intensité en fonction du nombre d'indice par pixel (attention avec dtype=np.uint8 255 est la valeur max)

# Afficher l'image

#Retournet l'image
#img = np.flipud(img) # Flip/mirroir

img = np.rot90(img, 2)   # Rotation à 180° / img = np.rot90(img, 1) pour 90

plt.figure(figsize=(18, 10))
plt.subplot(1, 1, 1) #2 lignes, 2 colonnes, 1er plot
plt.title("Coupe autour de Z=0")
plt.imshow(img, cmap='gray')
plt.axis('off') # pas d'axes sur le graphique

plt.show()

""" # Afficher l'image avec les couleurs inversée
img = np.invert(img)

plt.figure(figsize=(18, 10))
plt.subplot(1, 1, 1) #2 lignes, 2 colonnes, 1er plot
plt.title("Coupe autour de Z=0")
plt.imshow(img, cmap='gray')
plt.axis('off') # pas d'axes sur le graphique

plt.show()
 """
