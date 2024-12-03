import re

with open('input.txt') as data:
    instruction_codes = data.read()

mul_array = re.findall(r"mul\(\d{1,3},\d{1,3}\)", instruction_codes)

sum = 0
for mul in mul_array:
    figures = mul.replace('mul', '').replace('(', '').replace(')', '').split(',')
    sum += int(figures[0]) * int(figures[1])

print(sum)
