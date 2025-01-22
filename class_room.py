import random as r

class Room():
    room = []
    room_width = 4
    room_height = 4

    def __init__(self, room_width, room_height):
        self.room_width = room_width
        self.room_height = room_height
        self.generate_room()

    def generate_room(self):
        for height in range(0, self.room_height):
            width_list = []
            for width in range(0, self.room_width):
                width_list.append(bool(r.getrandbits(1)))
            self.room.append(width_list)
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
                    
