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

    game_id = game[5]
    set_strings = game[8:]
    
    blue = re.findall(r'\b(\d+)\s+blue\b', set_strings)
    red = re.findall(r'\b(\d+)\s+red\b', set_strings)
    green = re.findall(r'\b(\d+)\s+green\b', set_strings)

    blue_false = []
    green_false = []
    red_false = []

    blue_false = [blue_color for blue_color in blue if int(blue_color) > BLUE_THRESHOLD]
    red_false = [red_color for red_color in red if int(red_color) > RED_THRESHOLD]
    green_false = [green_color for green_color in green if int(green_color) > GREEN_THRESHOLD]

    print(blue_false)
    print(red_false)
    print(green_false)

    if len(blue_false) > 0 or len(green_false) > 0 or len(red_false) > 0: 
        break

    count += int(game_id)

print(count)