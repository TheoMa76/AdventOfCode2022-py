contenu = open("Day4\data.txt", "r")
lignes = contenu.readlines()
lignes = [ligne.strip() for ligne in lignes]
lignes = [ligne.split(",") for ligne in lignes]

somme = 0
nombres = []

for ligne in lignes:
    for nombre in ligne:
        nombres.append(nombre.split('-'))

for i in range(len(nombres)-1):
        if():
            somme += 1

print(somme)