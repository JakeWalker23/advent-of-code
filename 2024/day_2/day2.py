with open('input.txt') as report:
    data = report.readlines()

length = len(data)

def check_difference(a, b):
    if abs(a - b) < 1 or abs(a - b) > 3:
        return False
    else:
        return True

sum = 0

for line in data:
    level = list(map(int, line.strip('\n').split(' ')))
    
    sort_asc = level == sorted(level)
    sort_desc = level == sorted(level, reverse=True)

    if sort_asc or sort_desc:
        for num in range(len(level) -1):
            current = level[num]
            next_num = level[num + 1]

            if not check_difference(current, next_num):
                sum += 1
                break
        
    else:
        sum += 1

print(length - sum)