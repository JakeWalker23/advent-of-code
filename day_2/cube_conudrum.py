import re

RED_THRESHOLD = 12
GREEN_THRESHOLD = 13
BLUE_THRESHOLD = 14

count = 0

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

    if check(blue, BLUE_THRESHOLD) or check(red, RED_THRESHOLD) or check(green, GREEN_THRESHOLD):
        continue

    count += int(game_id[0])
print(count)

