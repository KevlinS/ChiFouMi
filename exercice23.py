import random
import getpass

print("==============================")
print("____BIENVENUE SUR CHIFOUMI____")
print("==============================")
good_choice = ['p', 'c', 'f']
player =''
choixMenu = input("1. Player vs Computer\n2. Player vs Player\nVotre choix : ")

compteur = 0
score_comp = 0
score_player = 0
score_player2 = 0 

# La partie Player vs Computer
if choixMenu == '1':

    # Boucle de jeu jusqu'à 5 fois
    while compteur != 5:
        player = input("Faites votre choix (p)pierre (f)feuille ou (c)ciseau : ")
        player = player.lower()
        if compteur == 5:
            break

        # Choix de computer    
        r = random.random() 

        if r < 0.33:
            computer = 'f'
        elif r < 0.66:
            computer = 'c'
        else:
            computer = 'p'
        
            while not(player in good_choice):
                player = input("Faites votre choix (p)pierre (f)feuille ou (c)ciseau : ")
                player = player.lower()

        # Comparaison player avec computer
        if player == 'p': 
            if computer == 'p':
                print("computer :",computer,"\n""Le résultat est NUL")
                compteur = compteur + 1
            elif computer == 'c':
                print("computer :",computer,"\n""Vous avez GAGNE")
                score_player = score_player + 1
                compteur = compteur + 1
                print("1 point pour vous")
            else:
                print("computer :",computer,"\n""Vous avez PERDU")
                score_comp = score_comp + 1
                compteur = compteur + 1
                print("1 point pour computer")

        if player == 'c':
            if computer == 'p':
                print("computer :",computer,"\n""Vous avez PERDU")
                score_comp = score_comp + 1
                compteur = compteur + 1
                print("1 point pour computer")
            elif computer == 'c':  
                print("computer :",computer,"\n""Le résultat est NUL")
                compteur = compteur + 1
            else:
                print("computer :",computer,"\n""Vous avez GAGNE")
                score_player = score_player + 1
                compteur = compteur + 1
                print("1 point pour vous")
        if player == 'f':
            if computer == 'p':
                print("computer :",computer,"\n""Vous avez GAGNE")
                score_player = score_player + 1
                compteur = compteur + 1
                print("1 point pour vous")
            elif computer == 'c':
                print("computer :",computer,"\n""Vous avez PERDU")
                score_comp = score_comp + 1
                compteur = compteur + 1
                print("1 point pour computer")
            else:
                print("computer :",computer,"\n""Le résultat est NUL")
                compteur = compteur + 1

    # Le résultat final
    if score_comp > score_player:
        print("====Vous n'avez pas de chance, Vous avez perdu, score final:",score_comp, "pour computer et",score_player, "pour vous====")
    elif score_player > score_comp:
        print("====Felicitaion!!! Vous avez gagné, score final:",score_player, "pour vous et",score_comp, "pour computer====")
    else:
        print("====Le match est NUL, score final:",score_player, "pour vous et",score_comp, "pour computer====")
        print("-MATCH FINAL, DERNIERE CHANCHE-")
        player = input("Faites votre choix (p)pierre (f)feuille ou (c)ciseau : ")
        player = player.lower()
        while not(player in good_choice):
                player = input("Faites votre choix (p)pierre (f)feuille ou (c)ciseau : ")
                player = player.lower()
        if player == 'p':
            if computer == 'p':
                print("computer :",computer,"\n""Le résultat est NUL, le jeu est fini!")
            elif computer == 'c':
                print("computer :",computer,"\n""FELICITATION!!! Vous avez GAGNE")
            else:
                print("computer :",computer,"\n""Vous n'avez pas vraiment de chance, vous avez PERDU")
        if player == 'c':
            if computer == 'p':
                print("computer :",computer,"\n""Vous n'avez pas vraiment de chance, vous avez PERDU")
            elif computer == 'c':
                print("computer :",computer,"\n""Le résultat est NUL, le jeu est fini!")
            else:
                print("computer :",computer,"\n""FELICITAION!!! Vous avez GAGNE")
        if player == 'f':
            if computer == 'p':
                print("computer :",computer,"\n""FELICITAION!!! Vous avez GAGNE")
            elif computer == 'c':
                print("computer :",computer,"\n""Vous n'avez pas vraiment de chance, vous avez PERDU")
            else:
                print("computer :",computer,"\n""Le résultat est NUL, le jeu est fini!")

# La partie Player vs Player     
if choixMenu == '2':
    # Boucle de jeu jusqu'à 5 fois
    while compteur != 5:
        player1 = getpass.getpass("PLAYER 1 - Faites votre choix (p)pierre (f)feuille ou (c)ciseau : ")
        player2 = getpass.getpass("PLAYER 2 - Faites votre choix (p)pierre (f)feuille ou (c)ciseau : ")
        if compteur == 5:
            break
        
            while not(player1 in good_choice):
                player1 = getpass.getpass("Faites votre choix (p)pierre (f)feuille ou (c)ciseau : ")

        
            while not(player2 in good_choice):
                player2 = getpass.getpass("Faites votre choix (p)pierre (f)feuille ou (c)ciseau : ")

        if player1 == 'p': # Comparaison player avec player 2
            if player2 == 'p':
                print("Le résultat est NUL")
                compteur = compteur + 1
            elif player2 == 'c':
                print("Player 1 a GAGNE")
                score_player = score_player + 1
                compteur = compteur + 1
                print("1 point pour player 1")
            else:
                print("Player 2 a GAGNE")
                score_player2 = score_player2 + 1
                compteur = compteur + 1
                print("1 point pour player 2")

        if player1 == 'c':
            if player2 == 'p':
                print("Player 2 a GAGNE")
                score_player2 = score_player2 + 1
                compteur = compteur + 1
                print("1 point pour player 2")
            elif player2 == 'c':  
                print("Le résultat est NUL")
                compteur = compteur + 1
            else:
                print("Player1 a GAGNE")
                score_player = score_player + 1
                compteur = compteur + 1
                print("1 point pour player 1")

        if player1 == 'f':
            if player2 == 'p':
                print("Player 1 a GAGNE")
                score_player = score_player + 1
                compteur = compteur + 1
                print("1 point pour player 1")
            elif player2 == 'c':
                print("Player 2 a GAGNE")
                score_player2 = score_player2 + 1
                compteur = compteur + 1
                print("1 point pour computer")
            else:
                print("Le résultat est NUL")
                compteur = compteur + 1

    # Le résultat final
    if score_player2 > score_player: 
        print("====Felicitaion!!! Player 2 a gagné, score final:",score_player2, "pour player 2 et",score_player, "pour player 1====")
    elif score_player > score_player2:
        print("====Felicitaion!!! Player 1 a gagné, score final:",score_player, "pour player 1 et",score_player2, "pour player 2====")
    else:
        print("====Le match est NUL, score final:",score_player, "pour player 1 et",score_player2, "pour player 2====")
        print("-MATCH FINAL, DERNIERE CHANCHE-")
        player1 = getpass.getpass("Faites votre choix (p)pierre (f)feuille ou (c)ciseau : ")
        player2 = getpass.getpass("Faites votre choix (p)pierre (f)feuille ou (c)ciseau : ")
        while not(player1 in good_choice):
                player1 = getpass.getpass("Faites votre choix (p)pierre (f)feuille ou (c)ciseau : ")

        while not(player2 in good_choice):
                player2 = getpass.getpass("Faites votre choix (p)pierre (f)feuille ou (c)ciseau : ")
                
        if player1 == 'p':
            if player2 == 'p':
                print("Le résultat est NUL, le jeu est fini!")
            elif player2 == 'c':
                print("FELICITATION!!! player 1 a GAGNE")
            else:
                print("FELICITATION!!! player 2 a GAGNE")
        if player1 == 'c':
            if player2 == 'p':
                print("FELICITATION!!! player 2 a GAGNE")
            elif player2 == 'c':
                print("Le résultat est NUL, le jeu est fini!")
            else:
                print("FELICITATION!!! player 1 a GAGNE")
        if player1 == 'f':
            if player2 == 'p':
                print("FELICITAION!!! player 1 a GAGNE")
            elif player2 == 'c':
                print("FELICITATION!!! player 2 a GAGNE")
            else:
                print("Le résultat est NUL, le jeu est fini!")