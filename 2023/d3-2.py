f = open("input3.txt", "r")
lines=f.readlines()
f.close()

for index, line in enumerate(lines):
    lines[index]=line.replace("\n","")
    
def isNumero(carattere):
    return carattere.isnumeric()

def findNumero(indexRiga, indexCarattere):
    if(not lines[indexRiga][int(indexCarattere)].isnumeric()):
        raise Exception("Carattere non numerico")
    stringaNumero = ""
    estremo1Caratteri=0
    estremo2Caratteri=len(lines[indexRiga])-1
    #caratteri prima
    i = 1
    while(1):
        if(int(indexCarattere)-i<estremo1Caratteri):
            break
        if(isNumero(lines[indexRiga][int(indexCarattere)-i])):
            stringaNumero = lines[indexRiga][int(indexCarattere)-i] + stringaNumero
        else:
            break
        i+=1
    #carattere iniziale
    stringaNumero+=lines[indexRiga][int(indexCarattere)]
    #caratteri dopo
    i = 1
    while(1):
        if(int(indexCarattere)+i>estremo2Caratteri):
            break
        if(isNumero(lines[indexRiga][int(indexCarattere)+i])):
            stringaNumero += lines[indexRiga][int(indexCarattere)+i]
        else:
            break
        i+=1
    return int(stringaNumero)

def checkAsterisco(indexRiga, indexCarattere):
    numeri = set()
    risultato=1
    #stessa riga
    #carattere prima
    if(indexCarattere != 0 and isNumero(lines[indexRiga][indexCarattere-1])):
        if len(numeri) < 2:
            numeri.add(findNumero(indexRiga, indexCarattere-1))
    #carattere dopo
    if(indexCarattere+1 < len(lines[indexRiga]) and isNumero(lines[indexRiga][indexCarattere+1])):
        if len(numeri) < 2:
            numeri.add(findNumero(indexRiga, indexCarattere+1))
    
    #riga prima
    if indexRiga != 0:
        #carattere stesso
        if(isNumero(lines[indexRiga-1][indexCarattere])):
            if len(numeri) < 2:
                numeri.add(findNumero(indexRiga-1, indexCarattere))
        #carattere prima
        if(indexCarattere != 0 and isNumero(lines[indexRiga-1][indexCarattere-1])):
            if len(numeri) < 2:
                numeri.add(findNumero(indexRiga-1, indexCarattere-1))
        #carattere dopo
        if(indexCarattere+1 < len(lines[indexRiga-1]) and isNumero(lines[indexRiga-1][indexCarattere+1])):
            if len(numeri) < 2:
                numeri.add(findNumero(indexRiga-1, indexCarattere+1))
        
    #riga dopo
    if indexRiga != len(lines)-1:
        #carattere stesso
        if(isNumero(lines[indexRiga+1][indexCarattere])):
            if len(numeri) < 2:
                numeri.add(findNumero(indexRiga+1, indexCarattere))
        #carattere prima
        if(indexCarattere != 0 and isNumero(lines[indexRiga+1][indexCarattere-1])):
            if len(numeri) < 2:
                numeri.add(findNumero(indexRiga+1, indexCarattere-1))
        #carattere dopo
        if(indexCarattere+1 < len(lines[indexRiga+1]) and isNumero(lines[indexRiga+1][indexCarattere+1])):
            if len(numeri) < 2:
                numeri.add(findNumero(indexRiga+1, indexCarattere+1))
    
    for numero in numeri:
        risultato*=numero
    return risultato if len(numeri) == 2 else 0
    
totale=0
for indexRiga, riga in enumerate(lines):
    indexCarattere = 0
    for carattere in riga:
        if carattere == "*":
            totale+=checkAsterisco(indexRiga, indexCarattere)
        indexCarattere+=1

print(totale)