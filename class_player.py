import random as r
from misc import *

class Player():
    pos = [0, 0]
    possible_movement_directions = [False, False, False, False] #0 = Up, 1 = Down, 2 = Left and 3 = Right
    selected_direction = -1
    debug = False
    move_flavour_text = ["You tread lightly; your weapon close to your chest.",
                         "You face the fear and move forward.",
                         "You make no sound as you tip toe forward.",
                         "You try to remain calm as you proceed.",
                         "You try to dispell the thoughts of your death as you sprint forward.",
                         "Now's not the time to panic; you dash forward."]

    teleport_flavour_text = ["The device on your wrist transports you to somewhere completely random.",
                             "A flick of the device on your wrist (and your wrist) and you're in a new place.",
                             "An orange glow on your wrist and, before you know it, the view is completely different.",
                             "Nanomachines take you apart and rebuild you in a completely random spot. Is it still you?",
                             "You find yourself teleported to a new location. Hopefully you don't have nightmares about that cat.",
                             "From here to there in under a second. Well, from your point of view at least."]

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

    wall_attacked_flavour_text = ["You shoot a wall. You're not sure if this out of panic or boredom or both.",
                                  "You shoot a wall. The wall is displeased.",
                                  "You brute! Shooting a wall like that! What did it do to you!",
                                  "Some of my best friends are walls. Please don't shoot them...",
                                  "Walls are friends, not food; Uhm, enimes...",
                                  "Nothing there but a wall...",
                                  "They're not like force fields, but walls can still stop bullets. So don't shoot them..."]

    monster_attacked_flavour_text = ["Monster down! Repeat, monster down! Good work agent!",
                                     "Good headshot. Monster down. Return to base agent.",
                                     "Swiss cheese. Good work agent, return to base.",
                                     "Your corporation is very pround of you agent. Truly. Return to base.",
                                     "Monster down. Return to base agent. No award this time, as usual.",
                                     "Good job agent. No promotion this time. Or ever really. Return to base.",
                                     "Boom. Good job. Return to base.",
                                     "Took you long enough agent. Return to base.",
                                     "Good job. Not enough to open the wine, but good job none the less. Return to base."]

    monster_missed_flavour_text = ["Miss. Do try better agent. We don't want this monster rampaging much longer.",
                                   "Nope... Nothing there. Well, back to hunting agent...",
                                   "Good thing your gun has a nanite chamber, huh? Please don't waste your infinite ammo though.",
                                   "Don't just fire your gun randomly agent. Try finding the monster first, eh?",
                                   "You weren't traind as a storm trooper, so don't shoot randomly like one; please."
                                   "Want to be retired from the corporation agent? We trained you better than that.",
                                   "Afraid we didn't supply you with homing bullets, agent. Please don't fire wildly or randomly.",
                                   "Need someone else to take over from you agent? Shoot the monster, not the air.",
                                   "We'd prefer it if you shot the wall. Then at least you'd be aiming at something!",
                                   "...Just shoot the monster, please?"]

    closeby_flavour_text = ["A loud roar fills you with dread, it seems to be all around you.",
                           "The ground quakes heavily all around; you catch your self from falling.",
                           "The monster must be close; its sounds are deafening.",
                           "Your heart is filled with dread; your ears are deafened; the monster is close.",
                           "You tread lightly, something tells you the monster is nearby. Perhaps it's how you've gone deaf?",
                           "The quakes from whatever is nearby cause you to nearly drop your weapon and cover your ears."]

    ontop_flavour_text = ["Do you enjoy that wall agent? Are you very much in pain agent?. Do you think another agent will suffice, agent? Maybe we shouldn't ask you since you'd be wrong.",
                          "Agent?! Agent?! Helloooooo?! Gah, another agent'll have to do.",
                          "Hmmm... Why is there a hole in your stomach? And, how are you still alive? Another agent is on their way. Not for you of course.",
                          "We need some help on aisle 10. And another agent.",
                          "Do try harder next time. Oh wait, you're dead. We'll train the next agent more. Maybe they won't be such a failure as you.",
                          "We thought you were qualified. A shame to see that even our agency can be wrong sometimes.",
                          "Oh, what a shame. How will we ever find another agent for this? Quite easily actually.",
                          "Enjoy your rest. You certainly haven't earned it. Another agent can pick up the slack.",
                          "We shan't let your next of kin know of your eternal slumber. Do you even have any kin?"]
                             

    def __init__(self, room, debug):
        self.pos[0] = -1
        self.pos[1] = -1
        self.move(room, True, True, True)
        self.selected_direction = 0
        self.debug = debug

    def move(self, room, move, no_print, is_random):
        if move is True:
            if is_random is True:
                rand_pos = room.get_random_pos()
                self.pos[0] = rand_pos[0]
                self.pos[1] = rand_pos[1]
                if no_print is False:
                    print_random_list(self.teleport_flavour_text)
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

    def ask_option(self, ask_move, is_attack):
        option = None
        if is_attack is True:
            while True:
                print("Do you want to attack North (N), East (E), South (S) or West (W)?")
                option = str(input("Option: ")).upper()
                if option != "N" and option != "NORTH" and option != "E" and option != "EAST" and option != "S" and option != "SOUTH" and option != "W" and option != "WEST":
                    print("Please enter a valid option")
                    pause()
                    print()
                else:
                    break
        if ask_move is True:
            while True:
                print("Do you want to Move (M), Rest (R), Attack (A) Teleport (T), or Quit (Q)?")
                option = str(input("Option: ")).upper()
                if option != "M" and option != "MOVE" and option != "R" and option != "REST" and option != "A" and option != "ATTACK" and option != "Q" and option != "QUIT" and option != "T" and option != "TELEPORT":
                    #Okay, this IF statement is getting a bit too long. Think of something to improve it perhaps?
                    print("Please enter a valid option")
                    pause()
                    print()
                else:
                    break
        else:
            if is_attack is False:
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

    def turn(self, room, monster):
        #ToDo: Check for if the player and monster are on top of each other (Player loss).
        room.show_pos_in_room(self.pos)
        if self.debug is True:
            print(self.pos)
            print("----------------------------------------------------------------")
            room.show_pos_in_room(monster.pos)
            print(monster.pos)
        print("")
        if monster.check_nearby(self) is True:
            print_random_list(self.closeby_flavour_text)
            pause()
            print("")
        room.describe_movement(self.pos, False)
        move_option = self.ask_option(True, False)
        if move_option == "R" or move_option == "REST":
            self.move(room, False, False, False)
        elif move_option == "A" or move_option == "ATTACK":
            move_option = self.ask_option(False, True)
            #Reusing the move_option variable here, but it is actually the direction the player wants to attack.
            if move_option == "N" or move_option == "NORTH":
                if room.spot_is_valid((self.pos[0], self.pos[1] - 1)) is True: #Check North is valid
                    if monster.check_hit((self.pos[0], self.pos[1] - 1)) is True:
                        print_random_list(self.monster_attacked_flavour_text) #Monster hit!
                        return 1
                    else:
                        print_random_list(self.monster_missed_flavour_text) #Monster not hit
                else:
                    print_random_list(self.wall_attacked_flavour_text) #Wall hit.
            elif move_option == "E" or move_option == "EAST": 
                if room.spot_is_valid((self.pos[0] + 1, self.pos[1])) is True: #Check East is valid
                    if monster.check_hit((self.pos[0] + 1, self.pos[1])) is True:
                        print_random_list(self.monster_attacked_flavour_text) #Monster hit!
                        return 1
                    else:
                        print_random_list(self.monster_missed_flavour_text) #Monster not hit
                else:
                    print_random_list(self.wall_attacked_flavour_text) #Wall hit.
            elif move_option == "S" or move_option == "SOUTH": 
                if room.spot_is_valid((self.pos[0], self.pos[1] + 1)) is True: #Check South is valid
                    if monster.check_hit((self.pos[0], self.pos[1] + 1)) is True:
                        print_random_list(self.monster_attacked_flavour_text) #Monster hit!
                        return 1
                    else:
                        print_random_list(self.monster_missed_flavour_text) #Monster not hit
                else:
                    print_random_list(self.wall_attacked_flavour_text) #Wall hit.
            elif move_option == "W" or move_option == "WEST": 
                if room.spot_is_valid((self.pos[0] - 1, self.pos[1])) is True: #Check West is valid
                    if monster.check_hit((self.pos[0] - 1, self.pos[1])) is True:
                        print_random_list(self.monster_attacked_flavour_text) #Monster hit!
                        return 1
                    else:
                        print_random_list(self.monster_missed_flavour_text) #Monster not hit
                else:
                    print_random_list(self.wall_attacked_flavour_text) #Wall hit.
            else:
                print("What... The bullet chose it's own path? What? Well it missed anyway...")
        elif move_option == "M" or move_option == "MOVE":
            move_option = self.ask_option(False, False)
            if move_option == "N" or move_option == "NORTH":
                if room.spot_is_valid((self.pos[0], self.pos[1] - 1)) is True: #Check North is valid
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
        elif move_option == "T" or move_option == "TELEPORT":
            self.move(room, True, False, True)
        elif move_option == "Q" or move_option == "QUIT":
            return 0
        else:
            print("Sorry, I think I had an error? What did you say?")
        
