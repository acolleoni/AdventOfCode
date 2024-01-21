file = open('input1.txt', 'r')
lines = file.readlines()

total = 0
for line in lines:
    firstDigit = None
    lastDigit = None
    for char in line:
        try:
            thisInteger = int(char)
            if firstDigit is None:
                firstDigit = thisInteger
            else:
                lastDigit = thisInteger
        except ValueError:
            continue

    if firstDigit is None:
        firstDigit = lastDigit
    if lastDigit is None:
        lastDigit = firstDigit
    number = int(str(firstDigit)+str(lastDigit))
    total += number

print(total)