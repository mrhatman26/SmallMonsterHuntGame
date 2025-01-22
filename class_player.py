class Player():
    pos [0, 0]
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
        self.move(room, True)

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
