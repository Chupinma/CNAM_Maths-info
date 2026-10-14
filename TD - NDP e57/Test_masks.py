from pye57 import E57
import numpy as np

filepath = r"E:\Maths-info\Cours\1.3 - Cours Fichier E57\E57\Ex1.e57"

with E57(filepath) as e57:

    Nb_points_total = 0

    for i in range(e57.scan_count):

        data = e57.read_scan(i, ignore_missing_fields=True)

        z = np.array(data["cartesianZ"])

        mask = np.abs(z) <= 0.01

        Nb_points = np.sum(mask)

        print("Scan", i, ":", Nb_points, "points")

        Nb_points_total += Nb_points

    print("Total :", Nb_points_total)