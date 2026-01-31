file = open('input4.txt', 'r')
lines = file.readlines()

result = 0
for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if char == '@':
            adj = 0
            if row - 1 >= 0 and col - 1 >= 0 and lines[row - 1][col - 1] == '@':
                adj += 1
            if row - 1 >= 0 and lines[row - 1][col] == '@':
                adj += 1
            if row - 1 >= 0 and col + 1 < len(line) and lines[row - 1][col + 1] == '@':
                adj += 1
            if col - 1 >= 0 and lines[row][col - 1] == '@':
                adj += 1
            if col + 1 < len(line) and lines[row][col + 1] == '@':
                adj += 1
            if row + 1 < len(lines) and col - 1 >= 0 and lines[row + 1][col - 1] == '@':
                adj += 1
            if row + 1 < len(lines) and lines[row + 1][col] == '@':
                adj += 1
            if row + 1 < len(lines) and col + 1 < len(line) and lines[row + 1][col + 1] == '@':
                adj += 1
            if adj < 4:
                result += 1
print(result)