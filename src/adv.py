from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


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

player = Player("Brennan", room['outside'])
def get_user_input():
    user_input = input("\nMenu\nn - north\ns - south\ne - east\nw - west\nq - quit\nPlease make a selection: ")
    return user_input


def move_rooms(input):
    switch = {
              'n': 'n_to',
              's': 's_to',
              'e': 'e_to',
              'w': 'w_to'
    }
    return switch.get(input, "error")


print(player.current_room.name)
print(player.current_room.description)
user_input = get_user_input()

while user_input != "q":
    proposed_move = getattr(player.current_room, move_rooms(user_input))
    if (proposed_move != "No room"):
        player.current_room = proposed_move
        print(player.current_room.name)
        print(player.current_room.description)
    else:
        print("\n*** Invalid move! Please make a different selection ***\n")
        print(player.current_room.name)
        print(player.current_room.description)
    user_input = get_user_input()
print('Thanks for playing! Goodbye!')
