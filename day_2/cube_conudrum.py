# Rules:

# Configuration: 12 red, 13 green, 14 blue

# Game # = ID 

# Each set is separated by ;

    # If a set is impossible, the game is void.

# Sum all of the game ID's that were possible.

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green POSSIBLE : 3 Sets 
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue POSSIBLE : 3 Sets 
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red IMPOSSIBLE

import re

RED_THRESHOLD = 12
GREEN_THRESHOLD = 13
BLUE_THRESHOLD = 14

count = 0

with open('input.txt', 'r') as file_input:
    games = file_input.readlines()


for game in games:

    # split into sets
    game_id = game[5]
    set_strings = game[8:]
    split_set_strings = set_strings.split(';')

    for set in split_set_strings.split(','):

        #IF set values do not exceed configuration
        print(set)

