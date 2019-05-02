"""
Exercice 23

JEU CHIFOUMI(Kevlin SUSANTO)

"""
import random

print("==============================")
print("____BIENVENUE SUR CHIFOUMI____")
print("==============================")
good_choice = ['pierre', 'ciseau', 'feuille']
player =''

compteur = 0
score_comp = 0
score_player = 0

while compteur != 5: # Boucle de jeu jusqu'à 5 fois
    player = input("Faites votre choix pierre feuille ou ciseau : ")
    player = player.lower()
    if compteur == 5:
        break
    r = random.random() # Choix de computer

    if r < 0.33:
        computer = 'feuille'
    elif r < 0.66:
        computer = 'ciseau'
    else:
        computer = 'pierre'
       
        while not(player in good_choice):
            player = input("Faites votre choix pierre feuille ou ciseau : ")
            player = player.lower()
    
    if player == 'pierre': # Comparaison player avec computer
        if computer == 'pierre':
            print("computer :",computer,"\n""Le résultat est NUL")
            compteur = compteur + 1
        elif computer == 'ciseau':
            print("computer :",computer,"\n""Vous avez GAGNE")
            score_player = score_player + 1
            compteur = compteur + 1
            print("1 point pour vous")
        else:
            print("computer :",computer,"\n""Vous avez PERDU")
            score_comp = score_comp + 1
            compteur = compteur + 1
            print("1 point pour computer")

    if player == 'ciseau':
        if computer == 'pierre':
            print("computer :",computer,"\n""Vous avez PERDU")
            score_comp = score_comp + 1
            compteur = compteur + 1
            print("1 point pour computer")
        elif computer == 'ciseau':  
            print("computer :",computer,"\n""Le résultat est NUL")
            compteur = compteur + 1
        else:
            print("computer :",computer,"\n""Vous avez GAGNE")
            score_player = score_player + 1
            compteur = compteur + 1
            print("1 point pour vous")
    if player == 'feuille':
        if computer == 'pierre':
            print("computer :",computer,"\n""Vous avez GAGNE")
            score_player = score_player + 1
            compteur = compteur + 1
            print("1 point pour vous")
        elif computer == 'ciseau':
            print("computer :",computer,"\n""Vous avez PERDU")
            score_comp = score_comp + 1
            compteur = compteur + 1
            print("1 point pour computer")
        else:
            print("computer :",computer,"\n""Le résultat est NUL")
            compteur = compteur + 1

if score_comp > score_player: # Le résultat final
    print("====Vous n'avez pas de chance, Vous avez perdu, score final:",score_comp, "pour computer et",score_player, "pour vous====")
elif score_player > score_comp:
    print("====Felicitaion!!! Vous avez gagné, score final:",score_player, "pour vous et",score_comp, "pour computer====")
else:
    print("====Le match est NUL, score final:",score_player, "pour vous et",score_comp, "pour computer====")
    print("-MATCH FINAL, DERNIERE CHANCHE-")
    player = input("Faites votre choix pierre feuille ou ciseau : ")
    player = player.lower()
    while not(player in good_choice):
            player = input("Faites votre choix pierre feuille ou ciseau : ")
            player = player.lower()
    if player == 'pierre':
        if computer == 'pierre':
            print("computer :",computer,"\n""Le résultat est NUL, le jeu est fini!")
        elif computer == 'ciseau':
            print("computer :",computer,"\n""FELICITATION!!! Vous avez GAGNE")
        else:
            print("computer :",computer,"\n""Vous n'avez pas vraiment de chance, vous avez PERDU")
    if player == 'ciseau':
        if computer == 'pierre':
            print("computer :",computer,"\n""Vous n'avez pas vraiment de chance, vous avez PERDU")
        elif computer == 'ciseau':
            print("computer :",computer,"\n""Le résultat est NUL, le jeu est fini!")
        else:
            print("computer :",computer,"\n""FELICITAION!!! Vous avez GAGNE")
    if player == 'feuille':
        if computer == 'pierre':
            print("computer :",computer,"\n""FELICITAION!!! Vous avez GAGNE")
        elif computer == 'ciseau':
            print("computer :",computer,"\n""Vous n'avez pas vraiment de chance, vous avez PERDU")
        else:
            print("computer :",computer,"\n""Le résultat est NUL, le jeu est fini!")