file = open('input4.txt', 'r')
lines = file.readlines()
file.close()

def algorythm():
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
                    lines[row] = lines[row][:col] + '.' + lines[row][col+1:]
    print(result)
    return result

total_result = 0
while True:
    current_result = algorythm()
    if current_result == 0:
        break
    total_result += current_result

print(total_result)