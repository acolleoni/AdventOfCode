lines = []
with open("input6.txt") as file:
    lines = file.readlines()

numbers = lines[: len(lines) - 1]
operations = lines[len(lines) - 1].split()

total = 0
problem_nr = 0
current_line_numbers = []
for i in range(len(numbers[0])):
    current_number = ""
    for j in range(len(numbers)):
        current_number += numbers[j][i]
    if current_number.strip() == "":
        if operations[problem_nr] == "*":
            line_total = 1
            for num in current_line_numbers:
                line_total *= num
        else:
            line_total = 0
            for num in current_line_numbers:
                line_total += num
        total += line_total
        problem_nr += 1
        current_line_numbers = []
    else:
        current_line_numbers.append(int(current_number))

print(total)
