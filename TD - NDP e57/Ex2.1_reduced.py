from pye57 import E57

filepath = r"E:\Maths-info\Cours\1.3 - Cours Fichier E57\E57\Ex1.e57"

with E57(filepath) as e57:

    Liste_X_tot = []
    Liste_Y_tot = []
    Liste_Z_tot = []

    for i in range(e57.scan_count):
        data = e57.read_scan(i, ignore_missing_fields=True)

        Liste_X_tot.extend(data["cartesianX"])
        Liste_Y_tot.extend(data["cartesianY"])
        Liste_Z_tot.extend(data["cartesianZ"])

print("Min en x =", round(min(Liste_X_tot), 2))
print("Max en x =", round(max(Liste_X_tot), 2))

print("Min en y =", round(min(Liste_Y_tot), 2))
print("Max en y =", round(max(Liste_Y_tot), 2))

print("Min en z =", round(min(Liste_Z_tot), 2))
print("Max en z =", round(max(Liste_Z_tot), 2))