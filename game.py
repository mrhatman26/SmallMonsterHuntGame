import platform, os, sys
from class_room import Room
from class_monster import Monster
from class_player import Player
from misc import *

#Get OS to determine what clear command to use
my_os = platform.system()
clear = None
if my_os == "Darwin" or my_os == "Linux":
    clear = lambda: os.system('clear')
else:
    clear = lambda: os.system('cls')
debug = ask_question("Debug?", "Enable debug mode?")
while True:
    #Setup game
    turns = 0
    while True:
        room = None
        try:
            del room
            room = Room(get_valid_number("Room Width: "), get_valid_number("Room Height: "), debug)
            break
        except Exception as e:
            print("So sorry, but I failed to make the gameboard. Please try again! I am very new to this!\nOh, and the exact problem was:\n\t" + str(e))
            pause()
            print("")
    monster = Monster(room)
    player = Player(room, debug)
    result = -1
    while True: #Actutal Game
        clear()
        print("Turns: " + str(turns))
        #Player's turn first
        result = player.turn(room, monster)
        if result == 0:
            sys.exit()
        if result == 1:
            print("You win!")
            pause()
            if ask_question("Play Again?", "Would you like to play again?") is False:
                sys.exit()
            else:
                break
        if monster.check_ontop(player) is True:
            print("\nYou died...")
            print_random_list(player.ontop_flavour_text)
            pause()
            if ask_question("Play Again?", "Would you like to play again?") is False:
                sys.exit()
            else:
                break
        pause()
        #Monster's turn next
        print()
        monster.move(room, False, False)
        pause()
        #Then finally, the room itself?
        room.move()
        turns += 1
