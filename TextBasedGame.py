
#William LaMarche IT-140


def instructions():
    print("Welcome to the game!\n")
    print("To play the game, you must enter commands.\n")
    print("To command your player to move from room to room, your first word will begin with 'go'\n (yes, lowercased), followed by a direction (as in 'West' - yes, with an uppercase)\n")
    print("Your directions include North, South, East and West. To exit the game, enter 'exit' \n")
    print("Some rooms will contain items. You are given an empty bag and your goal\n is to acquire all 6 items before entering the Lava Room.\n The lava Room is where your enemy awaits you. If you meet him, under prepared,\n you will...lose...to put it kindly.\n")
    print("To acquire each item, you will enter 'get' followed by the item that you see.\n")
    print("Enjoy!")



if __name__ == '__main__':
    castle_Rooms = {
        'Bedroom': {'South': 'Lava Room', 'West': 'Training Room'},
        'Training Room': {'South': 'Library', 'West': 'Closet', 'East': 'Bedroom', 'item': 'Wand'},
        'Closet': {'South': 'Shelter', 'East': 'Training Room', 'item': 'Cloak'},
        'Library': {'North': 'Training Room', 'West': 'Shelter', 'East': 'Lava Room', 'item': 'Wizardry Book'},
        'Shelter': {'North': 'Closet', 'South': 'Magic Room', 'East': 'Library', 'item': 'Loyal Pet'},
        'Magic Room': {'North': 'Shelter', 'East': 'Alchemy Center', 'item': 'Magic Carpet'},
        'Alchemy Center': {'West': 'Magic Room', 'North': 'Lava Room', 'item': 'Mana Potion'},
        'Lava Room': {'South': 'Alchemy Center', 'West': 'Library', 'North': 'Bedroom', 'item': 'Ghastly'},
    }

    print(instructions())


    playGame = ""
    room_status = "Bedroom"
    inventory = []


    while True:
        print("You are in:", room_status)
        print('Inventory: ', inventory)
        if 'item' in castle_Rooms[room_status]:
            print('You see a', castle_Rooms[room_status]['item'] + '.')
        playGame = input("What would you like to do?\n")
        splitStr = playGame.split()

        if splitStr[0] == "go":
            if splitStr[1] in castle_Rooms[room_status]:
                room_status = castle_Rooms[room_status][splitStr[1]]
            else:
                print("You can't go in that way!")

        elif splitStr[0] == "get":
            if 'item' in castle_Rooms[room_status]:
                if splitStr[1] in castle_Rooms[room_status]['item']:
                    if splitStr[1] in inventory:
                        print('You already acquired that item')
                    else:
                        inventory.append(castle_Rooms[room_status]["item"])
                        print('You have acquired a', castle_Rooms[room_status]["item"] + '!')
                else:
                    print('wrong item')
            else:
                print('No item in current room!')

        if room_status == 'Lava Room':
            print("MUAHAHAHAH.\n")
            print('*A ghostly figure appears*\n')
            if len(inventory) == 6:
                print("Adrenaline rises. The room's floor melts away to a boiling pool of lava.\n You are stuck at the entrance and don't know what to do. You look into your bag.\n You grab your wand and flicker away towards Ghastly. however, nothing happens.\n You see your book on Wizardy and read a quick spell. Wave your wand and nothing happens again!\n You look into the bag and see your cloak! You decide to put it on and retry waving your wand. \n Waila! It works! A bolt of lightning strikes Ghastly. Out flies your loyal Pet. A Hawk!\n Your hawk flies across the room to the injured Ghastly and finishes the job!\n Tired from the valiant fight, you look into your bag and find a mana potion, which you drink in one gulp.\n Lastly, you cross the lava, of course, on your magic flying carpet - and leave the castle - to freedom.\n")
                print("You have won the game.")
            else:
                print('You look into your bag and realize you do not have everything you need. In a flash, Ghastly approaches you and consumes your soul.\n You have lost the game. ')
            break



