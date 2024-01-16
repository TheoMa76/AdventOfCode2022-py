contenu = open("Day1\data.txt", "r")
lignes = contenu.readlines()
elfs = []
somme = 0
for ligne in lignes: #boucle pour chaque ligne
    if ligne.isspace(): #si la ligne est vide on ajoute la somme à la liste et on réinitialise la somme
        elfs.append(somme)
        somme = 0
    else: #sinon on ajoute la valeur de la ligne à la somme
        somme += int(ligne)

elfs.append(somme) #ajout de la dernière somme à la liste
print(max(elfs))