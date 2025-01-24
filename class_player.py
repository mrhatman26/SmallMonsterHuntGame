import random as r
from misc import *

class Player():
    pos = [0, 0]
    possible_movement_directions = [False, False, False, False] #0 = Up, 1 = Down, 2 = Left and 3 = Right
    move_flavour_text = ["You tread lightly; your weapon close to your chest.",
                         "You face the fear and move forward.",
                         "You make no sound as you tip toe forward.",
                         "You try to remain calm as you proceed.",
                         "You try to dispell the thoughts of your death as you sprint forward.",
                         "Now's not the time to panic; you dash forward."]

    sleep_flavour_text = ["You face remains pale as you sit idley.",
                          "A break: The only source of comfort in this place.",
                          "Nothing to eat; nothing to do. You sit in silence.",
                          "You can't stand the waiting, but you remain idle regardless.",
                          "You throw a rock at a wall like a tennis ball.",
                          "You wonder if there is anyone out there as you sit in silence.",
                          "You might be tired but your fear keeps you awake as you sit idle."]

    def __init__(self, room):
        self.pos[0] = -1
        self.pos[1] = -1
        self.move(room, True, False)

    def move(self, room, move, no_print):
        if move is True:
            rand_pos = room.get_random_pos()
            self.pos[0] = rand_pos[0]
            self.pos[1] = rand_pos[1]
            if no_print is False:
                print(self.move_flavour_text[r.randint(0, len(self.move_flavour_text) - 1)])
        else:
            if no_print is False:
                print(self.sleep_flavour_text[r.randint(0, len(self.move_flavour_text) - 1)])

    def ask_option(self):
        option = None
        while True:
            print("Do you want to Move (M) or Rest (R)?")
            str(input("Option: ")).upper()
            if option != "M" and option != "MOVE" and option != "R" and option != "REST":
                print("Please enter a valid option")
                pause()
                print()
            else:
                break
        return option

    def turn(self, room):
        room.show_pos_in_room(self.pos)
        room.describe_movement(self.pos)
