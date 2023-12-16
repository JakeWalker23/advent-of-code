import re

with open('input.txt', 'r') as file_input:
    boat_data = file_input.readlines()

boat_times = re.findall(r'\d+',boat_data[0])
boat_distances = re.findall(r'\d+', boat_data[1])

def calculate_race_distance(boat_time, winning_distance):
    winning_strategies = []

    for index in range(int(boat_time)):
        race_time = int(boat_time)
        charge = index
        time_to_race = race_time - charge

        distance_travelled = charge * time_to_race

        if int(distance_travelled) > int(winning_distance):
            winning_strategies.append(charge)

    return len(winning_strategies)


total = 1
for index_i, time in enumerate(boat_times):
    for index_j, distance in enumerate(boat_distances):

        if index_i == index_j:
            total *= calculate_race_distance(time, distance)


print(total)