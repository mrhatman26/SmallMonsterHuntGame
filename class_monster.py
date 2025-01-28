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

    sleep_flavour_text = ["All is calm.",
                         "Nothing makes a sound.",
                         "You sense nothing.",
                         "It's quiet.",
                         "Nothing on the ground moves an inch.",
                         "You hear nothing but your heartbeat.",
                         "A gust of wind goes by. It's calm."]

    move_chances = [False, False, False, True, True]
    
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
                rand_pos = room.get_random_pos()
                self.pos[0] = rand_pos[0]
                self.pos[1] = rand_pos[1]
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
            
