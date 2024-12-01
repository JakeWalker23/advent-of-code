import operator

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

sum = 0

for val in list(map(operator.sub, location_a, location_b)):
    sum += abs(val)

print(sum)