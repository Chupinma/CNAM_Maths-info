from pye57 import E57

# Ouvrir un fichier E57 complet
filepath = r"E:\Maths-info\Cours\1.3 - Cours Fichier E57\E57\Ex1.e57"
with E57(filepath) as e57:
    # Liste des scans présents
    Nb_scan = e57.scan_count
    
    Nb_points = 0

    for i in range(Nb_scan):
        data = e57.read_scan(i, ignore_missing_fields=True)
        Nb_points_scan = len(data["cartesianX"])
        Nb_points += Nb_points_scan
    print(Nb_points)