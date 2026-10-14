from pye57 import E57

# Ouvrir un fichier E57 complet
filepath = r"E:\Maths-info\Cours\1.3 - Cours Fichier E57\E57\Ex1.e57"
with E57(filepath) as e57:
    # Liste des scans présents
    Nb_scan = e57.scan_count

    # Création des listes vides de coordonnées
    Liste_X= []
    Liste_X_tot = []
    Liste_Y= []
    Liste_Y_tot = []
    Liste_Z= []
    Liste_Z_tot = []
    

    for i in range(Nb_scan) :
        data = e57.read_scan(i, ignore_missing_fields=True)

        # Lire la liste des coodonnées par scans et incémenter la liste totale pour tous les scans
        Liste_X = data["cartesianX"]
        Liste_X_tot.extend(Liste_X)

        Liste_Y = data["cartesianY"]
        Liste_Y_tot.extend(Liste_Y)

        Liste_Z = data["cartesianZ"]
        Liste_Z_tot.extend(Liste_Z)

# Trouver et afficher les valeurs min et max de chaques listes de coordonnées
Min_x = round(min(Liste_X),2)
Max_x = round(max(Liste_X),2)
print ("Min en x = ",Min_x)
print ("Max en x = ",Max_x)

Min_y = round(min(Liste_Y),2)
Max_y = round(max(Liste_Y),2)
print ("Min en y = ",Min_y)
print ("Max en y = ",Max_y)

Min_z = round(min(Liste_Z),2)
Max_z = round(max(Liste_Z),2)
print ("Min en z = ",Min_z)
print ("Max en z = ",Max_z)