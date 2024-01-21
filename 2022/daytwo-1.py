f = open("file2.txt", "r")
lines = f.readlines()

i=0
rounds = [0]

for line in lines:    
    
    if line[2] == "X": #Sasso
        rounds[i] += 1
        if line[0] == "A": #Sasso
            rounds[i] += 3
        if line[0] == "C": #Forbice
            rounds[i] += 6
    
    if line[2] == "Y": #Carta
        rounds[i] += 2
        if line[0] == "B": #Carta
            rounds[i] += 3
        if line[0] == "A": #Sasso
            rounds[i] += 6

    if line[2] == "Z": #Forbice
        rounds[i] += 3
        if line[0] == "C": #Forbice
            rounds[i] += 3
        if line[0] == "B": #Carta
            rounds[i] += 6          
    
    print(line)
    print(rounds[i])
    i=i+1
    rounds.append(0)    

f.close()

print(rounds)

ris=0
for round in rounds:
    ris += round
print(ris)