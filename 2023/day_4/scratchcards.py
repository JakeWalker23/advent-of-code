# Winning numbers are left of |

# 1 match is worth 1 points
    # each subsequent match doubles the value of points

# 1 match = 1 point
# 2 match = 2 points
# 3 match = 4 points
# 4 match = 8 points ... 

# Sum all of the points for all games


# Part 2:

# A matching number wins a copy of subsequent cards
    # Card 1 -> Matches = 5 -> Wins you a copy of Card 2,3,4,5,6
    # Card 2 -> Matches 


import re

with open('input.txt', 'r') as file_input:
    scratchcards = file_input.readlines()

points = 0

for line in scratchcards:
    # Can 'destructure' from the split
    scratchcard_winning, scratchcard_my_numbers = line[10:].strip().split(' | ')

    winning_numbers_string = re.findall(r'\d+', scratchcard_winning)
    my_numbers_string = re.findall(r'\d+', scratchcard_my_numbers)

    winning_numbers = [int(number) for number in winning_numbers_string]
    my_numbers = [int(my_number) for my_number in my_numbers_string]

    unique_winning_numbers = set(winning_numbers)
    unique_my_numbers = set(my_numbers)
    
    points_to_add = 0
    matches = []
    for number in unique_winning_numbers:
        if number in unique_my_numbers:
            matches.append(number)
            
            if len(matches) == 1:
                points_to_add += 1
                continue
                
            points_to_add *= 2

    points += points_to_add

print(points)