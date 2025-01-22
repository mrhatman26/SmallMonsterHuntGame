from class_room import Room
from class_monster import Monster

def get_valid_number(message):
    no = 0
    while True:
        try:
            no = int(input(message))
            break
        except:
            print("Please enter a valid number!")
            input("(Press ENTER to continue)")
            print()
    return no

room = Room(get_valid_number("Room Width: "), get_valid_number("Room Height: "))

'''while True:
    turns = 0
    room = Room(get_valid_number("Room Width: "), get_valid_number("Room Height: "))
    mon = Monster(room)
    while True:
        print("Turns: " + str(turns))
        x = 0
        while x < 10:
            mon.move(room, False)
            x += 1
        input()'''
