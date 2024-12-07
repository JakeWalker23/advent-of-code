with open('input.txt') as codes:
    data = codes.readlines()

all_results = []
total = 0
for code in data:
    test_score = int(code.split(':')[0])
    numbers = list(map(int, code.replace('\n', '').split(':')[1].split(' ')))

    stack = []
    results = []
    operators = ['+', '*']

    stack.append(([numbers[0]], numbers[1:]))

    while len(stack) > 0:
        current, remaining = stack.pop()

        if len(remaining) == 0:
            results.append(" ".join(map(str, current)))
            continue

        next_num = remaining[0]
        for operator in operators:
            new_expression = current + [operator, next_num]
            stack.append((new_expression, remaining[1:]))

    all_results.append({
        "test_score": test_score,
        "expressions": results
    })

for result in all_results:
    test_score = result['test_score']
    expressions = result['expressions']
    valid = False

    for expression in expressions:
        tokens = expression.split()
        current_value = int(tokens[0])

        for i in range(1, len(tokens), 2):
            operator = tokens[i]
            next_number = int(tokens[i + 1])

            if operator == '+':
                current_value += next_number
            elif operator == '*':
                current_value *= next_number

        if current_value == test_score:
            valid = True
            break

    if valid:
        total += test_score

print(f"Total Test Score: {total}")
