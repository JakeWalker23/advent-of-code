# Rules:

    # Any number adjacent to a symbol is a part number

    # Periods are not symbols.

    # Symbols include: [*, +, /, @, #, %, =, $, &] Not exhaustive, check for more

    # Sum all the part numbers

    # Line length 141
    # lines 140
    # digit length 1-3

import re

SYMBOLS = r'[*+/@#%=$&]'

count = 0

with open('input.txt', 'r') as file_input:
    parts_input = file_input.readlines()

symbol_coordinates = []
found_array = []

# Loop through input
for line_index, line in enumerate(parts_input):
    symbol_x_coordinates = [(m.start(0), m.end(0)) for m in re.finditer(r'[*+/@#%=$&]', line)]

    # Find all symbol coordinates
    for coordinate in symbol_x_coordinates:
        symbol_coordinates.append([line_index + 1, coordinate[0]])


 
for line_index, line in enumerate(parts_input):

    for location in symbol_coordinates:
        print(line_index + 1, coordinate[0])
        


    # if line_index == 1 and line[7]:
        # print(line[7])

    # Have symbol [x,y] coordinates:
        # I can determine numbers in:
            # above:        [x, y-1]
            # top right:    [x+1, y-1]
            # top left:     [x-1, y-1]
            # right:        [x+1, y]
            # left:         [x-1, y]
            # bottom right: [x+1, y+1]
            # bottom left:  [x-1, y+1]
            # down:         [x, y+1]

    # I want to match the whole number
    # Add it and its [x,y] coordinates to found array



    # horizontal_part_numbers = re.findall(r'(?<=[*+/@#%=$&])\d{1,3}|\d{1,3}(?=[*+/@#%=$&])', line)
   
 

print(count)
    # if symbol
        # Look up, topright, right, bottomright, down, bottomleft, left, topleft
            # If number
                # Add to count
            # if not number
                 # continue
