import platform, os
from class_room import Room
from class_monster import Monster
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
    mon = Monster(room)
    while True: #Actutal Game
        print("Turns: " + str(turns))
        x = 0
        while x < 10:
            mon.move(room, False)
            x += 1
        input()
        clear()
        
                   
