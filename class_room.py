import random as r

class Room():
    room = []
    room_width = 4
    room_height = 4

    def __init__(self, room_width, room_height):
        self.room_width = room_width
        self.room_height = room_height
        self.generate_room(False)

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
                draw_lines = False
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
                    random_row = r.randint(0, len(self.room))
                    random_column = r.randint(0, len(self.room[random_row - 1]))
                    box_height = r.randint(random_row + 1, random_row + (len(self.room) - 1))
                    box_width = r.randint(random_column + 1, random_column + (len(self.room[random_row]) - 1))
                    print(box_width)
                    row = random_row
                    column = random_column
                    while row < len(self.room):
                        if row > box_height:
                            break
                        else:
                            while column < len(self.room[row]):
                                if column > box_width:
                                    break
                                else:
                                    self.room[row][column] = True
                                column += 1
                        row += 1
                spots_filled += 1
        self.describe_room()

    def describe_room(self):
        for row in self.room:
            for column in row:
                if column is True:
                    print("[ ]", end="")
                else:
                    print("[x]", end="")
            print()

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
        print(selected_column, "|", selected_row)
        return (selected_column, selected_row)
                    
