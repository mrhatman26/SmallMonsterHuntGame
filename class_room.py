import random as r

class Room():
    pos = [0, 0]
    room = []
    room_width = 4
    room_height = 4
    debug = False

    def __init__(self, room_width, room_height, debug):
        self.room_width = room_width
        self.room_height = room_height
        self.generate_room(False)
        self.pos[0] = -1
        self.pos[1] = -1
        self.debug = debug
        self.move()

    def generate_room(self, old_gen):
        if old_gen is True:
            for height in range(0, self.room_height):
                width_list = []
                for width in range(0, self.room_width):
                    width_list.append(bool(r.getrandbits(1)))
                self.room.append(width_list)
        else:
            #Create all room spots (Starting as False)
            for row in range(0, self.room_height):
                width_list = []
                for column in range(0, self.room_width):
                    width_list.append(False)
                self.room.append(width_list)
            #Amount of times random spots are added is random
            random_spots = r.randint(2, 6) + 1
            spots_filled = 0
            while spots_filled < random_spots:
                #Random rooms (boxes) or lines
                draw_lines = bool(r.getrandbits(1))
                if draw_lines is True:
                    #Select random spots and add line from start to end.
                    from_left = bool(r.getrandbits(1))
                    if from_left is True:
                        #Add line from left to right
                        random_row = r.randint(0, len(self.room) - 1)
                        column = 0
                        while column < len(self.room[random_row]):
                            self.room[random_row][column] = True
                            column += 1
                    else:
                        #Add line from top to bottom
                        random_column = r.randint(0, len(self.room[0]) - 1)
                        row = 0
                        while row < len(self.room):
                            self.room[row][random_column] = True
                            row += 1
                else:
                    #Select random spots and create boxes.
                    random_row = r.randint(0, len(self.room) - 1)
                    random_column = r.randint(0, len(self.room[random_row]) - 1)
                    box_height = r.randint(2, int(len(self.room) / 2))
                    box_width = r.randint(2, int(len(self.room[random_row]) / 2))
                    row = random_row
                    row_counter = 0
                    column = random_column
                    column_counter = 0
                    while row_counter < len(self.room) - 1:
                        column_counter = 0
                        print("------------START LOOP------------")
                        if row_counter > random_row + box_height or row + row_counter > len(self.room):
                            print("[ROW BREAK]")
                            break
                        else:
                            while column_counter < len(self.room[row]):
                                if column_counter > random_column + box_width or column + column_counter > len(self.room[row]) - 1:
                                    print("[COLUMN BREAK]")
                                    break
                                else:
                                    print("row_counter = " + str(row_counter) + "\ncolumn_counter = " + str(column_counter) + "\nrandom_row + box_height = " + str(random_row + box_height) + "\nrandom_column + box_width = " + str(random_column + box_width))
                                    try:
                                        self.room[row + row_counter][column + column_counter] = True
                                    except Exception as e:
                                        print(e)
                                column_counter += 1
                        row_counter += 1
                    print("------------END LOOP------------")
                spots_filled += 1
                #For now, the generation may not link rooms together.
                #Teleporting is a solution for now, but
                #It should be fixed.
        self.print_room()

    def print_room(self):
        for row in self.room:
            for column in row:
                if column is True:
                    print("[ ]", end="")
                else:
                    print("[x]", end="")
            print()

    def describe_movement(self, current_pos):
        possible_movement_directions = [False, False, False, False] #0 = Up, 1 = Down, 2 = Left and 3 = Right
        #Check above pos
        if current_pos[1] > 0:
            if self.room[current_pos[1] - 1][current_pos[0]] == True:
                possible_movement_directions[0] = True
                print("You can move North from here")
        #Check below pos
        if current_pos[1] < self.room_height - 1:
            if self.room[current_pos[1] + 1][current_pos[0]] == True:
                possible_movement_directions[1] = True
                print("You can move South from here")
        #Chceck left pos
        if current_pos[0] > 0:
            if self.room[current_pos[1]][current_pos[0] - 1] == True:
                possible_movement_directions[2] = True
                print("You can move West from here")
        #Check right pos
        if current_pos[0] < self.room_width - 1:
            if self.room[current_pos[1]][current_pos[0] + 1] == True:
                possible_movement_directions[3] = True
                print("You can move East from here")
        return possible_movement_directions

    def show_pos_in_room(self, pos):
        row = 0
        column = 0
        while row < len(self.room):
            column = 0
            while column < len(self.room[row]):
                if row == pos[1] and column == pos[0]:
                    print("[!]", end="")
                else:
                    if self.room[row][column] is True:
                        print("[ ]", end="")
                    else:
                        print("[x]", end="")
                column += 1
            print()
            row += 1

    def get_random_pos(self):
        while True:
            selected_row = r.randint(0, len(self.room) - 1)
            if len(self.room[selected_row]) >= 1:
                selected_column = r.randint(0, len(self.room[selected_row]) - 1)
                if self.room[selected_row][selected_column] is True:
                    break
        #print(selected_column, "|", selected_row)
        return (selected_column, selected_row)

    def move(self):
        rand_pos = self.get_random_pos()
        self.pos[0] = rand_pos[0]
        self.pos[1] = rand_pos[1]

    def spot_is_valid(self, test_pos):
        try:
            if self.room[test_pos[1]][test_pos[0]] == True:
                return True
            else:
                return False
        except:
            return False
                    
