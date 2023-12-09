import re

RED_THRESHOLD = 12
GREEN_THRESHOLD = 13
BLUE_THRESHOLD = 14

count = 0
total = 0

def check(list1, val):
    return(any(int(x) > val for x in list1))

with open('input.txt', 'r') as file_input:
    games = file_input.readlines()

for game in games:
    game_id = re.findall(r'\bGame\s+(\d+)\b', game)

    set_strings = game[8:]
    
    blue = re.findall(r'\b(\d+)\s+blue\b', set_strings)
    red = re.findall(r'\b(\d+)\s+red\b', set_strings)
    green = re.findall(r'\b(\d+)\s+green\b', set_strings)

    blue_max = max(list(map(int, blue)))
    red_max = max(list(map(int, red)))
    green_max = max(list(map(int, green)))

    power = blue_max * red_max * green_max

    total += power

    # Commented out for part 2
    # if check(blue, BLUE_THRESHOLD) or check(red, RED_THRESHOLD) or check(green, GREEN_THRESHOLD):
    #     continue

    # count += int(game_id[0])
print(count)
print(total)

# part 2:
    # Select the highest value from each game
    # power = Multiply them all together
    # Sum all of the powers
