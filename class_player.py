import random as r
from misc import *

class Player():
    pos = [0, 0]
    possible_movement_directions = [False, False, False, False] #0 = Up, 1 = Down, 2 = Left and 3 = Right
    selected_direction = -1
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

    hit_wall_flavour_text = ["There's a wall there. The price is a headache.",
                             "Your head hurts. Why did you walk into a wall?",
                             "You thought you saw a doorway; your new headache says otherwise.",
                             "You hit a wall; You're head hurts.",
                             "Walls hurt. This wall is no different"]
                             

    def __init__(self, room):
        self.pos[0] = -1
        self.pos[1] = -1
        self.move(room, True, True, True)
        self.selected_direction = 0

    def move(self, room, move, no_print, is_random):
        if move is True:
            if is_random is True:
                rand_pos = room.get_random_pos()
                self.pos[0] = rand_pos[0]
                self.pos[1] = rand_pos[1]
                if no_print is False:
                    print_random_list(self.move_flavour_text)
            else:
                if self.selected_direction == 0:
                    self.pos[1] -= 1
                    print_random_list(self.move_flavour_text)
                elif self.selected_direction == 1:
                    self.pos[0] += 1
                    print_random_list(self.move_flavour_text)
                elif self.selected_direction == 2:
                    self.pos[1] += 1
                    print_random_list(self.move_flavour_text)
                elif self.selected_direction == 3:
                    self.pos[0] -= 1
                    print_random_list(self.move_flavour_text)
                else:
                    print("I was told to move you but... I forgot where? I'll leave you there for now...")
        else:
            if no_print is False:
                print_random_list(self.sleep_flavour_text)

    def ask_option(self, ask_move):
        option = None
        if ask_move is True:
            while True:
                print("Do you want to Move (M), Rest (R), Attack (A) Teleport (T) or Quit (Q)?")
                option = str(input("Option: ")).upper()
                if option != "M" and option != "MOVE" and option != "R" and option != "REST" and option != "A" and option != "ATTACK" and option != "Q" and option != "QUIT":
                    print("Please enter a valid option")
                    pause()
                    print()
                else:
                    break
        else:
            while True:
                print("Do you want to move North (N), East (E), South (S) or West (W)?")
                option = str(input("Option: ")).upper()
                if option != "N" and option != "NORTH" and option != "E" and option != "EAST" and option != "S" and option != "SOUTH" and option != "W" and option != "WEST":
                    print("Please enter a valid option")
                    pause()
                    print()
                else:
                    break
        return option

    def turn(self, room):
        room.show_pos_in_room(self.pos)
        room.describe_movement(self.pos)
        move_option = self.ask_option(True)
        if move_option == "R" or move_option == "REST":
            self.move(room, False, False, False)
        elif move_option == "M" or move_option == "MOVE":
            move_option = self.ask_option(False)
            if move_option == "N" or move_option == "NORTH":
                if room.spot_is_valid((self.pos[0], self.pos[1] - 1)) is True:
                    self.selected_direction = 0
                    self.move(room, True, False, False)
                else:
                    print_random_list(self.hit_wall_flavour_text)
            elif move_option == "E" or move_option == "EAST":
                if room.spot_is_valid((self.pos[0] + 1, self.pos[1])) is True:
                    self.selected_direction = 1
                    self.move(room, True, False, False)
                else:
                    print_random_list(self.hit_wall_flavour_text)
            elif move_option == "S" or move_option == "SOUTH":
                if room.spot_is_valid((self.pos[0], self.pos[1] + 1)) is True:
                    self.selected_direction = 2
                    self.move(room, True, False, False)
                else:
                    print_random_list(self.hit_wall_flavour_text)
            elif move_option == "W" or move_option == "WEST":
                if room.spot_is_valid((self.pos[0] - 1, self.pos[1])) is True:
                    self.selected_direction = 3
                    self.move(room, True, False, False)
                else:
                    print_random_list(self.hit_wall_flavour_text)
            else:
                print("Sorry, my ears are ringing... " + str(move_option) + " can't be what you said... Right?")
        elif move_option == "Q" or move_option == "QUIT":
            return 0
        else:
            print("Sorry, I think I had an error? What did you say?")
        
