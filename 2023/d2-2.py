file = open('input2.txt', 'r')
lines = file.readlines()

for i, line in enumerate(lines):
    lines[i] = line.replace("\n","")

totalPower = 0
for line in lines:
    #print(line)
    gameId = line.split(": ")[0].split(" ")[1]

    finalRed = 0
    finalGreen = 0
    finalBlue = 0
    for round in line.split(": ")[1].split("; "):
        #print(round)
        red = 0
        green = 0
        blue = 0
        #print(round)
        if "," in round:
            #print(True)
            for info in round.split(", "):
                if info.split(" ")[1] == "blue":
                    blue+=int(info.split(" ")[0])
                elif info.split(" ")[1] == "red":
                    red+=int(info.split(" ")[0])
                elif info.split(" ")[1] == "green":
                    green+=int(info.split(" ")[0])
        else:
            #print("'"+round.split(" ")[0]+"'")
            #print("'"+round.split(" ")[1]+"'")
            if round.split(" ")[1] == "blue":
                blue += int(round.split(" ")[0])
            elif round.split(" ")[1] == "red":
                red += int(round.split(" ")[0])
            elif round.split(" ")[1] == "green":
                green += int(round.split(" ")[0])
        #print(str(blue)+" are blue")
        #print(str(red)+" are red")
        #print(str(green)+" are green")
        #print()
        if(finalBlue < blue):
            finalBlue=blue
        if (finalRed < red):
            finalRed = red
        if (finalGreen < green):
            finalGreen = green

    totalPower+=finalBlue*finalRed*finalGreen


print(totalPower)

file.close()