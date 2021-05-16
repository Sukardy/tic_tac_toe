
blok_nummer1 = 1 
blok_nummer2 = 2
blok_nummer3 = 3
blok_nummer4 = 4
blok_nummer5 = 5
blok_nummer6 = 6
blok_nummer7 = 7
blok_nummer8 = 8
blok_nummer9 = 9


def playgrid():
    print("╔" + 3*"═" + "╦" + 3*"═" + "╦" + 3*"═" + "╗")
    print("║", blok_nummer1,"║", blok_nummer2, "║", blok_nummer3, "║")
    print("╠" + 3*"═" + "╬" + 3*"═" + "╬" + 3*"═" + "╣" )
    print("║", blok_nummer4, "║" , blok_nummer5,  "║", blok_nummer6, "║")
    print("╠" + 3* "═" + "╬" + 3*"═" + "╬" + 3*"═" + "╣")
    print("║", blok_nummer7, "║", blok_nummer8, "║", blok_nummer9, "║")
    print("╚" + 3*"═" + "╩" + 3*"═" + "╩" + 3*"═" + "╝")

def player_win():
    print()
    print("Tic tac toe speler",player, "heeft gewonnen!")
    global game
    game = False           

def winning_check():
    if blok_nummer1 !="" and blok_nummer1 == blok_nummer2 and blok_nummer2 == blok_nummer3:
        player_win()
    elif blok_nummer4 !="" and blok_nummer4 == blok_nummer5 and blok_nummer5 == blok_nummer6:
        player_win()
    elif blok_nummer7 !="" and blok_nummer7 == blok_nummer8 and blok_nummer8 == blok_nummer9:
        player_win()
    elif blok_nummer1 !="" and blok_nummer1 == blok_nummer4 and blok_nummer4 == blok_nummer7:
        player_win()    
    elif blok_nummer2 !="" and blok_nummer2 == blok_nummer5 and blok_nummer5 == blok_nummer8:
        player_win()
    elif blok_nummer3 !="" and blok_nummer3 == blok_nummer6 and blok_nummer6 == blok_nummer9:
        player_win()
    elif blok_nummer1 !="" and blok_nummer1 == blok_nummer5 and blok_nummer5 == blok_nummer9:
        player_win()
    elif blok_nummer3 !="" and blok_nummer3 == blok_nummer5 and blok_nummer5 == blok_nummer7:
        player_win()
    

moves = 9
x = int(input("Kies een nummer,(1) of (2). Welke speler gaat beginnen?:"))
player = x
playgrid()
game = True 
while game == True:
    if player == 1:
        character = "X"
    else:
        character = "O"   
    print()
    print("Speler", player, "voer een bloknummer in : ", end = " " )
    position = int(input())
    print()
    if position < 1 or position > 9:
        print("Het ingevoerde bloknummer is buiten bereik, probeer opnieuw!")
        print()
        continue
    if position == 1:
        if blok_nummer1 == "X" or blok_nummer1 == "O":
            print("Blok reeds in gebruik!")
            continue
        else:
            blok_nummer1 = character
            playgrid()
    if position == 2:
        if blok_nummer2 == "X" or blok_nummer2 == "O":
            print("Blok reeds in gebruik!")
            continue
        else:
            blok_nummer2 = character
            playgrid()
    if position == 3:
        if blok_nummer3 == "X" or blok_nummer3 == "O":
            print("Blok reeds in gebruik!")
            continue
        else:
            blok_nummer3 = character
            playgrid()
    if position == 4:
        if blok_nummer4 == "X" or blok_nummer4 == "O":
            print("Blok reeds in gebruik!")
            continue
        else:
            blok_nummer4 = character
            playgrid()
    if position == 5:
        if blok_nummer5 == "X" or blok_nummer5 == "O":
            print("Blok reeds in gebruik!")
            continue
        else:
            blok_nummer5 = character
            playgrid()
    if position == 6:
        if blok_nummer6 == "X" or blok_nummer6 == "O":
            print("Blok reeds in gebruik!")
            continue
        else:
            blok_nummer6 = character
            playgrid()
    if position == 7:
        if blok_nummer7 == "X" or blok_nummer7 == "O":
            print("Blok reeds in gebruik!")
            continue
        else:
            blok_nummer7 = character
            playgrid()
    if position == 8:
        if blok_nummer8 == "X" or blok_nummer8 == "O":
            print("Blok reeds in gebruik!")
            continue
        else:
            blok_nummer8 = character
            playgrid()
    if position == 9:
        if blok_nummer9 == "X" or blok_nummer1 == "O":
            print("Blok reeds in gebruik!")
            continue
        else:
            blok_nummer9 = character
            playgrid()          
    moves -=1 
    if game == True and moves == 0:
        print()
        print("gelijk spel!")
        break
    if moves < 5:
        winning_check()
    if player == 1:
        player += 1
    else:
        player -=1
    
        
print(3*"\n")
input("Press any key to quit :")