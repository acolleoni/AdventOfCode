input='''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''

splitInput=input.split("\n")

def checkLine(line):
    invalidLine = False
    ascending = False
    for index, value in enumerate(line):
        if(index==len(line)-1):
            continue
        if abs(int(line[index+1])-int(line[index]))>3:
            invalidLine=True
            break
        if int(line[index])==int(line[index+1]):
            invalidLine=True
            break
        if index == 0:
            if int(line[0])<int(line[1]):
                ascending = True
                continue
        if ascending:
            if int(line[index])>int(line[index+1]):
                invalidLine=True
                break
        else:
            if int(line[index])<int(line[index+1]):
                invalidLine=True
                break
    return invalidLine

safeLevels=0
for line in splitInput:
    splitLine = line.split(" ")
    invalidLine = checkLine(splitLine)
    if invalidLine:
        for errorIndex in range(len(splitLine)):
            newLine = [num for index, num in enumerate(splitLine) if index != errorIndex]
            invalidLine = checkLine(newLine)
            if not invalidLine:
                break
    if not invalidLine:
        safeLevels+=1

print(safeLevels)