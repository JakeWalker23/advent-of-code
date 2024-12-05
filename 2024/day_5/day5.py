with open('input.txt') as instructions:
	data = instructions.read()

pages = data.split('\n\n')[0].split('\n')
updates = data.split('\n\n')[1].split('\n')

total = 0

for update in updates:
	update = list(map(int, update.split(',')))
	
	for page in pages:
		X = int(page.split('|')[0])
		Y = int(page.split('|')[1])


		if X in update and Y in update:
			if update.index(X) < update.index(Y):
				continue
			else: 
				break

	else: 
		idx = len(update) // 2
		total += int(update[idx])