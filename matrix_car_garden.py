from os import system

# parking2d = parking
# pi = place index
# ri = row index

parking = [
    ["🚘", "🆓", "🆓", "🆓", "🆓"],
    ["🆓", "🚘", "🚘", "🆓", "🚘"],
    ["🚘", "🆓", "🚘", "🆓", "🚘"],
    ["🆓", "🚘", "🆓", "🚘", "🆓"],
]

# render
while True:
    system("cls")
    for ri in range(len(parking)):
        for pi in range(len(parking[ri])):
            print("|",parking[ri][pi], sep="",end=" |")

        print()
        print("-----" * len(parking[ri]))
    print("")
    print()
    # stats

    cars = 0
    free = 0
    for ri in range(len(parking)):
        for pi in range(len(parking[ri])):
            if parking[ri][pi] == "🚘":
                cars += 1
            else:
                free += 1
    
    cars_prc = cars * 100 / (len(parking) * len(parking[ri]))

    print(f"Cars on park: {cars} / {cars_prc:3.2f}% ")
    print("Free places: ", free)

    print("\n")

    print(
        "ACTIONS\n",
    )
    menu = {"actions": ["Park", "Drive out", "Repark", "Exit"]}
    for menu_num in range(len(menu["actions"])):
        print(menu_num + 1, menu["actions"][menu_num])

    action = int(input(">"))

    # ACTION SELECTION
    ##################################################### 1
    if action == 1:
        while True:
            idxr = int(input("To row?: "))
            idxr -= 1
            if idxr < len(parking):
                idxp = int(input("Place number?: "))
                idxp -= 1
                if idxp < len(parking[ri]):
                    if parking[idxr][idxp] == "🆓":
                        parking[idxr][idxp] = "🚘"
                        break
                    else:
                        print("Place are not available!")
                else:
                    print("You dont have so musch places!")
            else:
                print("You dont have so musch rows!")
    ##################################################### 2
    if action == 2:
        while True:
            idxr = int(input("From row?: "))
            idxr -= 1
            if idxr < len(parking):
                idxp = int(input("Place number?: "))
                idxp -= 1
                if idxp < len(parking[ri]):
                    if parking[idxr][idxp] == "🚘":
                        parking[idxr][idxp] = "🆓"
                        break
                    else:
                        print("Place was empty befor!")
                else:
                    print("You dont have so musch places!")
            else:
                print("You dont have so musch rows!")
    ##################################################### 3
    if action == 3:
        while True:
            idxr = int(input("From row?: "))
            idxr -= 1
            if idxr > len(parking):
                print("You dont have so musch rows!")
                continue
            idxp = int(input("From place number?: "))
            idxp -= 1
            if idxp > len(parking[ri]):
                print("You dont have so musch places!")
                continue
            elif parking[idxr][idxp] == "🆓":
                print("Nothing to repark!")
                continue
            idxr2 = int(input("To row?: "))
            idxr2 -= 1
            if idxr2 > len(parking):
                print("You dont have so musch rows!")
                continue
            idxp2 = int(input("To place number?: "))
            idxp2 -= 1
            if idxp2 > len(parking[ri]):
                print("You dont have so musch places!")
                continue
            elif parking[idxr2][idxp2] == "🚘":
                print("Place are not available!!")
                continue
            if parking[idxr][idxp] == "🚘" and parking[idxr2][idxp2] == "🆓":
                parking[idxr][idxp] = "🆓"
                parking[idxr2][idxp2] = "🚘"
                break

    ##################################################### 4
    if action == 4:
        system("cls")
        print("Exit")
        break
