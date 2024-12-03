f = open("input-4.txt", "r")
originalText = f.read()
f.close()

def findPositionValue(text, position):
    result=(-1,-1,-1)
    newPos=position+4
    while True:
        if not text[newPos].isnumeric():
            break
        newPos = newPos+1
    if newPos == position+4:
        return (-1,-1,-1)
    result = (newPos, -1, -1)
    if not text[newPos]==",":
        return (-1,-1,-1)
    newPos=newPos+2
    result=(result[0], newPos, -1)
    while True:
        if not text[newPos].isnumeric():
            break
        newPos = newPos+1
    if not text[newPos]==")":
        return (-1,-1,-1)
    return (result[0], result[1], newPos)

def notInactive(text, position):
    if(text[:position].rfind("don't") == -1):
        return True
    return text[:position].rfind("do(") >= text[:position].rfind("don't")

text=originalText
total=0
absolutePosition=0
while True:
    foundPosition = text.find("mul(")
    absolutePosition=absolutePosition+foundPosition+8
    if text == "" or foundPosition == -1:
        break
    endPosition = findPositionValue(text, foundPosition)
    if(endPosition != (-1,-1,-1) and notInactive(originalText, absolutePosition)):
        total += int(text[foundPosition+4:endPosition[0]]) * int(text[endPosition[1]-1:endPosition[2]])
    text = text[foundPosition+8:]

print(total)