file = open('input1.txt', 'r')
lines = file.readlines()
backup = lines.copy()

# First Literal Digit Substitution
validLiteralDigits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
firstDigitList = []
lastDigitList = []
found=False
for i, line in enumerate(lines):
    buffer = ""
    for char in line:
        buffer += char
        found = False
        for literalDigit in validLiteralDigits:
            if buffer.__contains__(literalDigit):
                firstDigitList.append(validLiteralDigits.index(literalDigit)+1)
                found=True
                break
            elif char.isnumeric():
                firstDigitList.append(int(char))
                found=True
                break
        if found:
            break

# Last Literal Digit Substitution
for i, line in enumerate(lines):
    buffer = ""
    for char in line[::-1]:
        buffer = char + buffer
        found = False
        for literalDigit in validLiteralDigits:
            if buffer.__contains__(literalDigit):
                lastDigitList.append(validLiteralDigits.index(literalDigit)+1)
                found=True
                break
            elif char.isnumeric():
                lastDigitList.append(int(char))
                found=True
                break
        if found:
            break

total=0
for index,number in enumerate(firstDigitList):
    total += int(str(number) + str(lastDigitList[index]))

print(total)
file.close()