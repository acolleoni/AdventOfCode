file = open('input2.txt', 'r')
lines = file.readlines()

class Game:
    def __init__(self, id, red, green, blue):
        self.id=0
        self.red=0
        self.blue=0
        self.green=0
        self.id=id
        self.red=red
        self.blue=blue
        self.green=green
    def __str__(self):
        return str("Game "+str(self.id)+": "+str(self.red)+" red; "+str(self.blue)+" blue; "+str(self.green)+" green")

games = []

for i, line in enumerate(lines):
    lines[i] = line.replace("\n","")

totalValidGames = 0
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
        if(finalBlue<blue):
            finalBlue=blue
        if (finalRed < red):
            finalRed = red
        if (finalGreen < green):
            finalGreen = green

    if(finalBlue<=14 and finalRed<=12 and finalGreen<=13):
        totalValidGames+=int(gameId)

    #games.append(Game(gameId, finalRed, finalGreen, finalBlue))

'''for game in games:
    print(str(game))

for game in games:'''

print(totalValidGames)

file.close()