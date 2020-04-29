from room import Room
from item import Item

class Player:
    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    def __str__(self):
        return f"{self.name}, {self.current_room}, {self.items}"

    def __repr__(self):
        return f"Name: {self.name}, Current Room: {self.current_room}, Inventory: {self.items}"

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

    def get_item(self, item):
        if item in self.current_room.items:
            self.current_room.items.remove(item)
            self.items.append(item)

    def drop_item(self, item):
        if item in self.items:
            self.items.remove(item)
            self.current_room.items.append(item)