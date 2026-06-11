lines = []
with open("input6.txt") as file:
    lines = [line.strip().split() for line in file]

numbers = lines[: len(lines) - 1]
operations = lines[len(lines) - 1]
total = 0
for i in range(len(numbers[0])):
    if operations[i] == "*":
        line_total = 1
        for j in range(len(numbers)):
            line_total *= int(numbers[j][i])
    else:
        line_total = 0
        for j in range(len(numbers)):
            line_total += int(numbers[j][i])
    total += line_total

print(total)
