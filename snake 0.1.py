from os import system
from random import randint
system ("cls")

########## DATE ##########
player = 11
box = randint(1,100)
if box == player:
    box = box + 1 or box - 1 or box+10 or box-10
score = 0
body = 0

while True:
    system("cls")
    ########## MAP ##########
    print("\n")
    for x in range (1,101):
        if x == player:         # PLAYER
            print("⬜", end="")
            if player % 10 == 0:
                print("")
        ##############################
        elif player == box:
            box = randint(1, 100)
            score += 1
        elif x == box:          # BOX
            print("🞖 ", end="")
            if box % 10 == 0:
                print("")
        ##############################
        else:
            print("⬛", end="") # ZONE
            if x %10==0:
                print()
    ########## INPUT ##########
    print(f"Score {score}\n")

    direction = input("Select direction(W/A/S/D)>")
    if direction == "w" and player - 10 >= 1:
        player -= 10
    if direction == "a" and player % 10 != 1:
        player -= 1
    if direction == "s" and player + 10 < 101:
        player += 10
    if direction == "d" and player % 10 != 0:
        player += 1


# ⬛ Zone
# ⬜ Player
# 🞖 BOX
