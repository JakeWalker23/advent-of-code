# Winning numbers are left of |

# 1 match is worth 1 points
    # each subsequent match doubles the value of points

# 1 match = 1 point
# 2 match = 2 points
# 3 match = 4 points
# 4 match = 8 points ... 

# Sum all of the points for all games

import re

with open('input.txt', 'r') as file_input:
    scratchcards = file_input.readlines()

points = 0

for line in scratchcards:
    scratchcard_numbers = line[10:].strip().split(' | ')

    winning_numbers = re.findall(r'\d{2}', scratchcard_numbers[0])
    my_numbers = re.findall(r'\d{2}', scratchcard_numbers[1])

    int_winning_numbers = [int(number) for number in winning_numbers]
    int_my_numbers = [int(my_number) for my_number in my_numbers]

    match = []
    for number in int_my_numbers:
        if number in int_winning_numbers:
            match.append(number)
    

    if len(match) == 1:
        points += 1

    # Over complicated. 
    # Should take into account non unique my_numbers
     
    if len(match) > 1:
        points += (int(len(match)) - 1) * 2

print(points)





    # return the length of my_numbers in winning_numbers
        # Should be counted once unless its in twice
    
    # total += len(length of my_numbers in winning_numbers) * 2