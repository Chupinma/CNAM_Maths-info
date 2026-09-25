import numpy as np
import open3d as o3d
from pye57 import E57

filepath = r"D:\01_Travail_Etudes\01_Ecoles\CNAM\M2_2026-2027\Maths-info\Cours\1.3 - Cours Fichier E57\E57\Ex2.e57"

# 1) Lecture du scan E57 avec pye57
e57 = E57(filepath)
data = e57.read_scan(0, ignore_missing_fields=True)
points = np.column_stack((data["cartesianX"], data["cartesianY"], data["cartesianZ"]))

# 2) Construction du nuage Open3D (pas de fichier intermédiaire)
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)
print("Nombre de points avant :", len(pcd.points))

# 3) Voxélisation : un point représentatif par voxel de 5 cm
taille_voxel = 0.005
pcd_voxel = pcd.voxel_down_sample(voxel_size=taille_voxel)

print("Nombre de points après :", len(pcd_voxel.points))

# 4) Visualisation du résultat
o3d.visualization.draw_geometries([pcd_voxel], point_show_normal=True)