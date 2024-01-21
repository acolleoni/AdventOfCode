f = open("input4.txt", "r")
lines=f.readlines()
f.close()

totalPoints=0
cardNumbers = [1]*len(lines)
for index, line in enumerate(lines):
    cardNumber=line.split(":")[0].split(" ")[1]
    winningNumbers=line.split(":")[1].replace("\n","").split(" | ")[0].split(" ")
    extractedNumbers=line.split(":")[1].replace("\n","").split(" | ")[1].split(" ")
    matchPoints=0
    for extractedNumber in extractedNumbers:
        if extractedNumber != '' and extractedNumber in winningNumbers:
            matchPoints+=1
    for i in range(cardNumbers[index]):
        counter=matchPoints
        for cardIndex, card in enumerate(cardNumbers):
                if(cardIndex>index):
                    cardNumbers[cardIndex]=card+1
                    counter-=1
                if(counter==0):
                    break

total=0
for number in cardNumbers:
    total += number
print(total)