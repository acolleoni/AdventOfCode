f = open("input4.txt", "r")
lines=f.readlines()
f.close()

totalPoints=0
for line in lines:
    cardNumber=line.split(":")[0].split(" ")[1]
    winningNumbers=line.split(":")[1].replace("\n","").split(" | ")[0].split(" ")
    extractedNumbers=line.split(":")[1].replace("\n","").split(" | ")[1].split(" ")
    matchPoints=0
    first=True
    for extractedNumber in extractedNumbers:
        if extractedNumber != '' and extractedNumber in winningNumbers and first == True:
            matchPoints+=1
            first = False
        elif extractedNumber != '' and extractedNumber  in winningNumbers:
            matchPoints*=2
    totalPoints+=matchPoints
    
print(totalPoints)