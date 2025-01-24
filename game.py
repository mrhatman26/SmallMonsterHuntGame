import platform, os
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
while True:
    #Setup game
    debug = False
    turns = 0
    room = Room(get_valid_number("Room Width: "), get_valid_number("Room Height: "), debug)
    monster = Monster(room)
    player = Player(room)
    while True: #Actutal Game
        clear()
        print("Turns: " + str(turns))
        #Player's turn first
        player.turn(room)
        pause()
        #Monster's turn next
        print()
        monster.move(room, False)
        pause()
        #Then finally, the room itself?
        room.move()
        turns += 1
