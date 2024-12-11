with open('input.txt') as content:
	data = content.read().split()
	
stones = [int(x) for x in data]



# Rules

# If 0, replace with 1
# lenth is even, replace with 2 stones. 1st = left side of half, 2nd right side of half
# If none of above rules apply, * 2024


for _ in range(25):
	output = []
	for stone in stones:
		if stone == 0:
			output.append(1)
			continue
		string = str(stone)
		length = len(string)
		if length % 2 == 0:
			output.append(int(string[:length // 2]))
			output.append(int(string[length // 2:]))	
		else:
			output.append(stone * 2024)

	stones = output
	

print(len(stones))




# return the length of the array
