import numpy as np

f = open("input4.txt", "r")
matrix = np.array([list(line.strip()) for line in f.readlines()])
f.close()

def checkValid(matrix,i,j):
    if matrix[i+1,j+1] != 'A':
        return False
    if not ((matrix[i,j] == 'M' and matrix[i+2,j+2] == 'S') or (matrix[i,j] == 'S' and matrix[i+2,j+2] == 'M')):
        return False
    if not ((matrix[i+2,j]== 'M' and matrix[i,j+2] == 'S') or (matrix[i+2,j]== 'S' and matrix[i,j+2] == 'M')):
        return False
    return True

numOfValidOccurrences = 0
for i, line in enumerate(matrix):
    for j, character in enumerate(line):
        try:
            #print(matrix[i+1,j+1], matrix[i,j], matrix[i+2,j+2], matrix[i+2,j], matrix[i,j+2], numOfValidOccurrences)
            if checkValid(matrix, i, j):
                numOfValidOccurrences += 1
        except:
            pass

print(numOfValidOccurrences)