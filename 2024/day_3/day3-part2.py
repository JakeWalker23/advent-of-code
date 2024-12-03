import re

with open('input.txt') as data:
    instruction_codes = data.read()

matches = [match.group() for match in re.finditer(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", instruction_codes)]



do_array = []
skip_flag = False

for match in matches:
    if match == "don't()":
        skip_flag = True
        continue

    if match == "do()":
        skip_flag = False
        continue

    if skip_flag == False:
        do_array.append(match)

sum = 0
for val in do_array:
    figures = val.replace('mul', '').replace('(', '').replace(')', '').split(',')
    sum += int(figures[0]) * int(figures[1])

print(sum)