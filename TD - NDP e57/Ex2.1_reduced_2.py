from pye57 import E57
import numpy as np

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

points = np.column_stack(( Liste_X_tot, Liste_Y_tot, Liste_Z_tot ))

# Calculer le coin minimal du nuage
mini = points.min(axis=0)
maxi = points.max(axis=0)

print("Min en =", mini)
print("Max en =", maxi)
