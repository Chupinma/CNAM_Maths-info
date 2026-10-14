from pye57 import E57

# Ouvrir un fichier E57 complet
filepath = r"E:\Maths-info\Cours\1.3 - Cours Fichier E57\E57\Ex1.e57"
with E57(filepath) as e57:
	  # Liste des scans présents
	  print("Nombre de scans :", e57.scan_count)