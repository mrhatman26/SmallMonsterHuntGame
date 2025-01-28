import random as r
from misc import print_random_list

class Monster():
    pos = [0, 0]
    move_flavour_text = ["You hear a rumble in the distance.",
                         "You feel a slight quake running through the ground.",
                         "A roar echoes all around you.",
                         "You see crows flying suddenly in to the air.",
                         "You sense movement nearby.",
                         "A coin jumps up and down on the floor."]

    teleport_flavour_text = ["You hear the sound of nanomachines taking something apart in the distance.",
                             "You hear sci-fi noises in the distance. Someone's moved VERY quickly.",
                             "You hear something odd. Meanwhile, you swear something orange just flew by?",
                             "You hear something strange. Something move from here to there and FAST.",
                             "You wish you knew more ways to describe sci-fi noises. You assume something's teleported.",
                             "That noise! Did the monster just teleport?",
                             "Something orange wooshes past. It move from here to there in under a second you could say."]

    sleep_flavour_text = ["All is calm.",
                         "Nothing makes a sound.",
                         "You sense nothing.",
                         "It's quiet.",
                         "Nothing on the ground moves an inch.",
                         "You hear nothing but your heartbeat.",
                         "A gust of wind goes by. It's calm."]

    move_chances = [False, False, False, True, True]

    teleport_chances = [False, False, False, False, False, False, False, True]
    
    def __init__(self, room):
        self.pos[0] = -1
        self.pos[0] = -1
        self.move(room, True, True)

    def move(self, room, no_print, not_random):
        if not_random is True:
            rand_pos = room.get_random_pos()
            self.pos[0] = rand_pos[0]
            self.pos[1] = rand_pos[1]
            if no_print is False:
                print_random_list(self.move_flavour_text)
        else:
            if self.move_chances[r.randint(0, len(self.move_chances) - 1)] is True:
                if self.teleport_chances[r.randint(0, len(self.move_chances) - 1)] is True:
                    rand_pos = room.get_random_pos()
                    self.pos[0] = rand_pos[0]
                    self.pos[1] = rand_pos[1]
                    if no_print is False:
                        print_random_list(self.teleport_flavour_text)
                else:
                    available_directions = room.describe_movement(self.pos, True)
                    #print("Available Directions", available_directions)
                    available_direction_indexes = [index for index, direction in enumerate(available_directions) if direction is True]
                    #print("Available Direction Indexs", available_direction_indexes)
                    move_option = r.randint(0, len(available_direction_indexes) - 1)
                    #0 = Up, 1 = Down, 2 = Left, 3 = Right
                    if move_option == 0:
                        self.pos[1] -= 1
                    if move_option == 1:
                        self.pos[1] += 1
                    if move_option == 2:
                        self.pos[0] -= 1
                    if move_option == 3:
                        self.pos[0] += 1
                    if no_print is False:
                        print_random_list(self.move_flavour_text)
            else:
                if no_print is False:
                    print_random_list(self.sleep_flavour_text)

    def check_hit(self, attack_pos):
        if attack_pos[0] == self.pos[0] and attack_pos[1] == self.pos[1]:
            return True
        else:
            return False

    def check_nearby(self, player):
        try:
            #North
            if self.pos[0] == player.pos[0] and self.pos[1] - 1 == player.pos[1]:
                return True
            #East
            elif self.pos[0] + 1 == player.pos[0] and self.pos[1] == player.pos[1]:
                return True
            #South
            elif self.pos[0] == player.pos[0] and self.pos[1] + 1 == player.pos[1]:
                return True
            #West
            elif self.pos[0] - 1 == player.pos[0] and self.pos[1] == player.pos[1]:
                return True
            else:
                return False
        except:
            return False
            
