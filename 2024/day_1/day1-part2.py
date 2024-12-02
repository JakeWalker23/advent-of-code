from collections import Counter

with open("input.txt") as content:
    locations = content.readlines()

location_b = []
location_a = []

for location in locations:
    line = location.split('   ')
    
    location_a.append(int(line[0]))
    location_b.append(int(line[1]))

location_a.sort()
location_b.sort()

location_b_count = Counter(location_b)

similarity_score = 0

for location in location_a:
    if location in location_b_count:
        similarity_score += (location * location_b_count[location])

print(similarity_score)