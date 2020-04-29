class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f"{self.name}, {self.current_room}"

    def __repr__(self):
        return f"Name: {self.name}, Current Room: {self.current_room}"

    def try_north(self):
        if self.current_room.n_to != None: # If the room north of your current room isn't none
            self.current_room = self.current_room.n_to # Move north
        else:
            print("\n YOU CAN'T GO THAT WAY \n")

    def try_east(self):
        if self.current_room.e_to != None: # If the room east of your current room isn't none
            self.current_room = self.current_room.e_to # Move east
        else:
            print("\n YOU CAN'T GO THAT WAY \n")

    def try_south(self):
        if self.current_room.s_to != None: # If the room south of your current room isn't none
            self.current_room = self.current_room.s_to # Move south
        else:
            print("\n YOU CAN'T GO THAT WAY \n")

    def try_west(self):
        if self.current_room.w_to != None: # If the room west of your current room isn't none
            self.current_room = self.current_room.w_to # Move west
        else:
            print("\n YOU CAN'T GO THAT WAY \n")