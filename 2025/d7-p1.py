import numpy as np

with open("input7.txt") as file:
    matrix = np.array([list(line.strip()) for line in file.readlines()])

def propagateBeam(current_row, column):
    while current_row != matrix.shape[0]:
        if matrix[current_row][column] == ".":
            matrix[current_row][column] = "|"
        elif matrix[current_row][column] == "^":
            propagateBeam(current_row, column - 1)
            propagateBeam(current_row, column + 1)
            break
        else:
            break
        current_row += 1

column = np.where(matrix[0] == 'S')[0][0]
propagateBeam(1, column)

for row in matrix:
    print(''.join(row))

result=0
for row_num, row in enumerate(matrix[1:]):
    for char_num, char in enumerate(row):
        if char == "^":
            if matrix[row_num-1][char_num] == '|' or matrix[row_num-1][char_num] == 'S':
                result +=1

print()
print(result)