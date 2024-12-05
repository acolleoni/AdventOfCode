import numpy as np

def isXmas(charList):
    charString = ''.join(charList)
    return charString == 'XMAS' or charString == 'SAMX'

f = open("input4.txt", "r")
matrix = np.array([list(line.strip()) for line in f.readlines()])
f.close()

numOfValidInstances = 0
invertedMatrix = matrix[::-1]
for i, line in enumerate(matrix):
    for j, character in enumerate(line):
        if isXmas(matrix[i][j:j+4]):
            numOfValidInstances+=1
        if isXmas(matrix[i:i+4, j]):
            numOfValidInstances+=1
        if isXmas(np.diagonal(matrix[i:],j)[0:4]):
            numOfValidInstances+=1
        if isXmas(np.diagonal(invertedMatrix[i:],j)[0:4]):
            numOfValidInstances+=1

print(numOfValidInstances)