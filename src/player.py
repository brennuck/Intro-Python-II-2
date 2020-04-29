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
        if item in self.current_room.items: # If there is an item in the room
            self.current_room.items.remove(item) # Remove it from the room
            self.items.append(item) # Add to players items
            item.on_take() # Prints you picked up the item


    def drop_item(self, item):
        if item in self.items: # If there is an item in players inventory
            self.items.remove(item) # Remove it
            self.current_room.items.append(item) # Add it to the room inventory
            item.on_drop() # Prints you picked up the item

    def print_items(self):
        if len(self.items) > 0:
            item_list = "You are holding the following items:"
            for item in self.items:
                item_list += f"\n {item}"
        else:
            item_list = "You are not holding anything"
        print(item_list)