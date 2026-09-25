from pye57 import E57
import numpy as np
import matplotlib.pyplot as plt
import open3d as o3d

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

# Assembler les liste dans un tableau numpy
points = np.column_stack(( Liste_X_tot, Liste_Y_tot, Liste_Z_tot ))

# Calculer le coin minimal du nuage
mini = points.min(axis=0)

#afficher les coordonnées de mini
print ("Point minimal du nuage :",mini)

# Définir / créer la fonction de voxelisation
def voxelisation(points, taille_voxel):
    # points : tableau numpy de forme (N, 3) : N lignes (les points), 3 colonnes (x, y, z)
    # axis=0 signifie « on écrase l'axe 0 (les lignes) », donc le minimum est calculé colonne par colonne
    mini = points.min(axis=0) 

    # Indice de voxel (i, j, k) pour chaque point
    # np.floor renvoie des flottants (2.0, pas 2). On convertit en entiers avec .astype(int).
    indices = np.floor((points - mini) / taille_voxel).astype(int) 
    
    # Regrouper les points ayant le même indice de voxel
    voxels = {}
    # map(tuple, indices) convertit chaque ligne d'indices en tuple (i, j, k). 
    # Nécessaire pour utiliser comme clé de dictionnaire.
    for point, idx in zip(points, map(tuple, indices)): 
        voxels.setdefault(idx, []).append(point)

    # Un seul point représentatif par voxel : le centroïde
    points_voxelises = np.array([ np.mean(pts, axis=0) for pts in voxels.values() ])

    return points_voxelises, indices, voxels


# Variable de la taile des voxels
taille_voxel=0.002

# On applique la fonction qu'on à défini sur notre tableau numpy de points
nuage_reduit, indices, voxels = voxelisation(points, taille_voxel)
print("Points conservés :", len(nuage_reduit))

# Afficher le nombre de voxels sur chacun des axes x, y et z
Nb_voxels = indices.max(axis=0)+1
print("Voxels par axe (x, y, z) : ", Nb_voxels)

Voxel_pleins = np.unique(indices)
print (voxels)

# 2) Construction du nuage Open3D (pas de fichier intermédiaire)
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)
print("Nombre de points avant :", len(pcd.points))
