from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),
    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
}

sword = Item("Sword", "Dull but will do the trick")
fork = Item("Fork", "You imagine all the food you could be eating")

room['outside'].items = None
room['foyer'].items = None
room['overlook'].items = [sword]
room['narrow'].items = [fork]
room['treasure'].items = None


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player("Brennon", room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def move(player):
    print(f"\nCurrent room:{player.current_room}, \nItems in the room: {player.current_room.items}")
    direction_choice = input("\n Where would you like to go? n, e, s, w, or q to quit \n")

    if direction_choice == "n":
        print(f"\nCurrent room:{player.current_room}, \nItems in the room: {player.current_room.items}")
        player.try_north()
        move(player)
    elif direction_choice == "e":
        print(f"\nCurrent room:{player.current_room}, \nItems in the room: {player.current_room.items}")
        player.try_east()
        move(player)
    elif direction_choice == "s":
        print(f"\nCurrent room:{player.current_room}, \nItems in the room: {player.current_room.items}")
        player.try_south()
        move(player)
    elif direction_choice == "w":
        print(f"\nCurrent room:{player.current_room}, \nItems in the room: {player.current_room.items}")
        player.try_west()
        move(player)
    elif direction_choice == "q":
        print("Bye Bye")

move(player1)