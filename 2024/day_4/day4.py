with open('input.txt') as wordGrid:
    data = wordGrid.readlines()

match_count = 0
match_array = []

for i in range(len(data)):
    for j in range(len(data[i])): 
        if data[i][j] == 'X':
            if j + 3 < len(data[i]):
                if data[i][j+1] == 'M' and data[i][j+2] == 'A' and data[i][j+3] == 'S':
                    print(f"Horizontal right match at ({i}, {j})")
                    match_count += 1

            if j - 3 >= 0:
                if data[i][j-1] == 'M' and data[i][j-2] == 'A' and data[i][j-3] == 'S':
                    print(f"Horizontal left match at ({i}, {j})")
                    match_count += 1

            if i + 3 < len(data):
                print(f"vertical down match at ({i}, {j})")
                if data[i+1][j] == 'M' and data[i+2][j] == 'A' and data[i+3][j] == 'S':
                    match_count += 1

            if i - 3 >= 0:
                if data[i-1][j] == 'M' and data[i-2][j] == 'A' and data[i-3][j] == 'S':
                    print(f"vertical up match at ({i}, {j})")
                    match_count += 1
            
            if i - 3 >= 0 and j - 3 >= 0:
                if data[i-1][j-1] == 'M' and data[i-2][j-2] == 'A' and data[i-3][j-3] == 'S':
                    print(f"diagnol up left match at ({i}, {j})")
                    match_count += 1

            if i - 3 >= 0 and j + 3 < len(data[i]):
                if data[i-1][j+1] == 'M' and data[i-2][j+2] == 'A' and data[i-3][j+3] == 'S':
                    print(f"diagnol up right match at ({i}, {j})")
                    match_count += 1

            if i + 3 < len(data) and j + 3 < len(data[i]):
                if data[i+1][j+1] == 'M' and data[i+2][j+2] == 'A' and data[i+3][j+3] == 'S':
                    print(f"diagnol down right match at ({i}, {j})")
                    match_count += 1

            if i + 3 < len(data) and j - 3 >= 0:
                if data[i+1][j-1] == 'M' and data[i+2][j-2] == 'A' and data[i+3][j-3] == 'S':
                    print(f"diagnol down left match at ({i}, {j})")
                    match_count += 1

print(match_count)