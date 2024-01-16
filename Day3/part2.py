contenu = open("Day3\data.txt", "r")
lignes = contenu.readlines()
lignes = [ligne.strip() for ligne in lignes]

#creation de dictionnaire. i +96 car 97 à 122 dans ASCII c'est les lettre de a à z
values = {chr(i + 96): i for i in range(1, 27)}  # Pour minuscule
values.update({chr(i + 64): i + 26 for i in range(1, 27)}) # Pour majuscule

badge = []

groupe = []

for ligne in lignes:

    if(len(groupe) == 3):
        sets = [set(g) for g in groupe]
        #permet de trouver les éléments communs
        #*sets permet de passer tout les set d'un seul coup a la fonction intersection()
        
        itemCommun = set.intersection(*sets)
        #ajoute tout les item commun a la fin de la liste badge
        badge.extend(itemCommun)
        groupe = []
    
    groupe.append(ligne)

#ajout du dernier badge pour le dernier groupe
sets = [set(g) for g in groupe]
itemCommun = set.intersection(*sets)
badge.extend(itemCommun)

valeur = [values[letter] for letter in badge]

print(sum(valeur))
