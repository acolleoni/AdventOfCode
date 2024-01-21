f = open("file2.txt", "r")
lines = f.readlines()

i=0
rounds = [0]

#Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock
for line in lines:    
    
    if line[0] == "A": #AvversarioSceglieSasso
        if line[2] == "X": #Perdi->Forbice
            rounds[i] += 3
        if line[2] == "Y": #Patta->Sasso
            rounds[i] += (3+1)
        if line[2] == "Z": #Vinci->Carta
            rounds[i] += (6+2)
    
    if line[0] == "B": #AvversarioSceglieCarta
        if line[2] == "X": #Perdi->Sasso
            rounds[i] += 1
        if line[2] == "Y": #Patta->Carta
            rounds[i] += (3+2)
        if line[2] == "Z": #Vinci->Forbice
            rounds[i] += (6+3)
    
    if line[0] == "C": #AvversarioSceglieForbice
        if line[2] == "X": #Perdi->Carta
            rounds[i] += 2
        if line[2] == "Y": #Patta->Forbice
            rounds[i] += (3+3)
        if line[2] == "Z": #Vinci->Sasso
            rounds[i] += (6+1)
    
    i=i+1
    rounds.append(0)    

f.close()

print(rounds)

ris=0
for round in rounds:
    ris += round
print(ris)