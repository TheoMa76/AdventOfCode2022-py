contenu = open("Day2\data.txt", "r")
lignes = contenu.readlines()
#A,B,C = ROCK,PAPER,SCISSORS = 1,2,3
#X,Y,Z = ROCK,PAPER,SCISSORS = 1,2,3

win,draw,lose = 6,3,0
rock,paper,scissors = 1,2,3
lignes = [ligne.strip() for ligne in lignes]
lignes = [ligne.split(" ") for ligne in lignes]
score = 0
for ligne in lignes:
    for i in range(len(ligne)):
        if ligne[i] == "A":
            if ligne[i+1] == "X":
                score += draw + rock
            elif ligne[i+1] == "Y":
                score += win + paper
            elif ligne[i+1] == "Z":
                score += lose + scissors
        elif ligne[i] == "B":
            if ligne[i+1] == "X":
                score += lose + rock
            elif ligne[i+1] == "Y":
                score += draw + paper
            elif ligne[i+1] == "Z":
                score += win + scissors
        elif ligne[i] == "C":
            if ligne[i+1] == "X":
                score += win + rock
            elif ligne[i+1] == "Y":
                score += lose + paper
            elif ligne[i+1] == "Z":
                score += draw + scissors
print(score)