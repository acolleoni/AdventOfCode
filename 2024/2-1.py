input='''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''

splitInput=input.split("\n")

safeLevels=0
for line in splitInput:
    splitLine = line.split(" ")
    invalidLine=False
    ascending = False
    for index, value in enumerate(splitLine):
        if(index==len(splitLine)-1):
            continue
        if abs(int(splitLine[index+1])-int(splitLine[index]))>3:
            invalidLine=True
            break
        if int(splitLine[index])==int(splitLine[index+1]):
            invalidLine=True
            break
        if index == 0:
            if int(splitLine[0])<int(splitLine[1]):
                ascending = True
                continue
        if ascending:
            if int(splitLine[index])>int(splitLine[index+1]):
                invalidLine=True
                break
        else:
            if int(splitLine[index])<int(splitLine[index+1]):
                invalidLine=True
                break
    if not invalidLine:
        safeLevels+=1

print(safeLevels)