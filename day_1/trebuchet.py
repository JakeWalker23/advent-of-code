import re

with open("input.txt", "r") as input:
    # Read the contents of the file
    file_contents = input.readlines()

def find_calibration_digits_in_input(file_contents):
    digit_array = []

    string_to_integer_mapping = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    for line in file_contents:
        digit_array.append(re.findall('\d{1}|one|two|three|four|five|six|seven|eight|nine', line))

    for val in digit_array:
        for index, digit in enumerate(val):
            if digit in string_to_integer_mapping:
               val[index] = string_to_integer_mapping[digit]

    return digit_array

# Select 1st & last number of the line.
def select_calibration_values(calibration_values):
    sorted_calibration_values = []

    for value in calibration_values:
        if len(value) == 1:
            sorted_calibration_values.append([value[0], value[0]])
        else:
            sorted_calibration_values.append([value[0], value[-1]])
    
    return sorted_calibration_values

def join_sorted_calibrated_value(sorted_calibration_values):
    joined_calibration_values = []
    for calibration_value in sorted_calibration_values:
        joined_calibration_values.append("".join(calibration_value))
    
    return joined_calibration_values

def sum_calibration_values(joined_calibration_values):
    total = 0
    for value in joined_calibration_values:
        total += int(value)
    return total


calibration_values = find_calibration_digits_in_input(file_contents)
sorted_calibration_values = select_calibration_values(calibration_values)
joined_calibration_values = join_sorted_calibrated_value(sorted_calibration_values)

print(sum_calibration_values(joined_calibration_values))


# 0-500 -> 26338         | Mine -> 26330
# 501-1000 -> 27530      | Mine -> 27555
# 53868                  | Mine -> 53,885     17 out