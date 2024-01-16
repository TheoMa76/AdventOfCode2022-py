contenu = open("Day3\data.txt", "r")
lignes = contenu.readlines()
lignes = [ligne.strip() for ligne in lignes]

#creation de dictionnaire. i +96 car 97 à 122 dans ASCII c'est les lettre de a à z
values = {chr(i + 96): i for i in range(1, 27)}  # Pour minuscule
values.update({chr(i + 64): i + 26 for i in range(1, 27)}) # Pour majuscule

item = []

for ligne in lignes:

    mid = len(ligne) // 2  # Trouver l'index du milieu
    lignes1 = ligne[:mid]  # Prendre la première moitié
    lignes2 = ligne[mid:]  # Prendre la deuxième moitié

    # Convertir les listes en ensembles
    set1 = set(lignes1)
    set2 = set(lignes2)
    item.append(set1 & set2)

item = ''.join([list(i)[0] for i in item]) #permet de transformer la liste d'ensemble
# en une chaine de caractère
valeur = [values[letter] for letter in item]

print(sum(valeur))
