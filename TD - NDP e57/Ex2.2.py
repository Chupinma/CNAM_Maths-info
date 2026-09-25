from pye57 import E57
import numpy as np

filepath = r"E:\Maths-info\Cours\1.3 - Cours Fichier E57\E57\Ex2.e57"

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