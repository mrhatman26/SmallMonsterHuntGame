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

    closeby_flavour_text = ["A loud roar fills you with dread, it seems to be all around you.",
                           "The ground quakes heavily all around; you catch your self from falling.",
                           "The monster must be close; its sounds are deafening.",
                           "Your heart is filled with dread; your ears are deafened; the monster is close.",
                           "You tread lightly, something tells you the monster is nearby. Perhaps it's how you've gone deaf?",
                           "The quakes from whatever is nearby cause you to nearly drop your weapon and cover your ears."]

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
        if attack_pos[0] == pos[0] and attack_pos[1] == pos[1]:
            return True
        else:
            return False
                
