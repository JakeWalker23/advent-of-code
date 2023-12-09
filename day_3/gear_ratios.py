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
    print(parts_input)

for line in parts_input:
# horizontal test 1362
    print(re.findall(rf'(?<=[{SYMBOLS}])\d{{1,3}}(?={SYMBOLS})', line))
    # if re.findall(r'\b(\d+)\b', line):

    # if symbol
        # Look up, topright, right, bottomright, down, bottomleft, left, topleft
            # If number
                # Add to count
            # if not number
                # continue
