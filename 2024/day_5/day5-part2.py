with open('input.txt') as instructions:
	data = instructions.read()

pages = data.split('\n\n')[0].split('\n')
updates = data.split('\n\n')[1].split('\n')

total = 0

def move_x_before_y(update, x, y):
    index_x = update.index(x)
    index_y = update.index(y)

    update.pop(index_x)
    update.insert(index_y, x)


for update in updates:
    update = list(map(int, update.split(',')))
    is_incorrect = False

    for page in pages:
        X = int(page.split('|')[0])
        Y = int(page.split('|')[1])

        if X in update and Y in update:
            if update.index(X) > update.index(Y):
                is_incorrect = True
                break

    if is_incorrect:
        not_stable = True
        while not_stable:
            for page in pages:
                X = int(page.split('|')[0])
                Y = int(page.split('|')[1])

                if X in update and Y in update:
                    if update.index(X) > update.index(Y):
                        move_x_before_y(update, X, Y)

                        not_stable = True
                        break
            else:
                not_stable = False

        idx = len(update) // 2
        total += int(update[idx])

print(total)