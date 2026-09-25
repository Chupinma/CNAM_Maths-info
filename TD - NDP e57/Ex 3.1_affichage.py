from pye57 import E57
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# 1. Charger le fichier E57
# ============================================================

filepath = r"D:\01_Travail_Etudes\01_Ecoles\CNAM\M2_2026-2027\Maths-info\Cours\1.3 - Cours Fichier E57\E57\Ex2.e57"

with E57(filepath) as e57:

    Liste_X_tot = []
    Liste_Y_tot = []
    Liste_Z_tot = []

    # Parcourir tous les scans
    for i in range(e57.scan_count):

        data = e57.read_scan(i, ignore_missing_fields=True)

        Liste_X_tot.extend(data["cartesianX"])
        Liste_Y_tot.extend(data["cartesianY"])
        Liste_Z_tot.extend(data["cartesianZ"])


# ============================================================
# 2. Assembler les coordonnées dans un tableau (N, 3)
# ============================================================

points = np.column_stack((Liste_X_tot, Liste_Y_tot, Liste_Z_tot))


# ============================================================
# 3. Calculer le coin minimal du nuage
# ============================================================

mini = points.min(axis=0)

print("Point minimal du nuage :", mini)


# ============================================================
# 4. Fonction de voxelisation
# ============================================================

def voxelisation(points, taille_voxel):

    # Coin minimal du nuage
    mini = points.min(axis=0)

    # Calcul de l'indice de voxel de chaque point
    indices = np.floor(
        (points - mini) / taille_voxel
    ).astype(int)

    # Dictionnaire contenant les points de chaque voxel
    voxels = {}

    # Regrouper les points par voxel
    for point, idx in zip(points, map(tuple, indices)):

        voxels.setdefault(idx, []).append(point)

    # Calculer un centroïde par voxel
    points_voxelises = np.array([
        np.mean(pts, axis=0)
        for pts in voxels.values()
    ])

    return points_voxelises


# ============================================================
# 5. Voxelisation
# ============================================================

taille_voxel = 0.005

nuage_reduit = voxelisation(points, taille_voxel)

print("Points avant voxelisation :", len(points))
print("Points après voxelisation :", len(nuage_reduit))


# ============================================================
# 6. Fonction pour transformer un nuage 3D en image 2D
# ============================================================

def nuage_vers_image(points, largeur, hauteur, x_min, x_max, y_min, y_max):

    # Créer une image noire
    img = np.zeros((hauteur, largeur), dtype=np.uint8)

    # Transformer X en coordonnées de pixels
    x_indexed = np.interp(points[:, 0], [x_min, x_max], [0, largeur - 1])

    # Transformer Y en coordonnées de pixels
    y_indexed = np.interp(points[:, 1], [y_min, y_max], [0, hauteur - 1])

    # Transformer les coordonnées en entiers
    x_int = x_indexed.astype(np.int32)
    y_int = y_indexed.astype(np.int32)

    # Mettre les points en blanc
    img[y_int, x_int] = 255

    return img


# ============================================================
# 7. Paramètres de l'image
# ============================================================

Largeur = 800
Hauteur = 500


# ============================================================
# 8. Déterminer les mêmes limites X/Y pour les deux images
# ============================================================

x_min = points[:, 0].min()
x_max = points[:, 0].max()

y_min = points[:, 1].min()
y_max = points[:, 1].max()


# ============================================================
# 9. Créer l'image du nuage original
# ============================================================

img_originale = nuage_vers_image(
    points,
    Largeur,
    Hauteur,
    x_min,
    x_max,
    y_min,
    y_max
)


# ============================================================
# 10. Créer l'image du nuage voxelisé
# ============================================================

img_voxelisee = nuage_vers_image(
    nuage_reduit,
    Largeur,
    Hauteur,
    x_min,
    x_max,
    y_min,
    y_max
)


# ============================================================
# 11. Afficher les deux images
# ============================================================

plt.figure(figsize=(18, 8))

# Image avant voxelisation
img_originale = np.rot90(img_originale, 2)
img_originale = np.invert(img_originale)
plt.subplot(1, 2, 1)
plt.title("Avant voxelisation")
plt.imshow(img_originale, cmap="gray")
plt.axis("off")

# Image après voxelisation.
img_voxelisee = np.rot90(img_voxelisee, 2)
img_voxelisee = np.invert(img_voxelisee)
plt.subplot(1, 2, 2)
plt.title("Après voxelisation")
plt.imshow(img_voxelisee, cmap="gray")
plt.axis("off")

plt.show()