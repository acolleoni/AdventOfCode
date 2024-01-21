f = open("input3.txt", "r")
lines=f.readlines()
f.close()

for index, line in enumerate(lines):
    lines[index]=line.replace("\n","")
    
def isSimbolo(carattere):
    return (not carattere.isnumeric()) and carattere != "."
def isThereSimboloInLista(lista):
    for elemento in lista:
        if isSimbolo(elemento):
            return True
    return False

def checkNumero(numero, indexRiga, indexCarattereIniziale):
    indexCarattereFinale=indexCarattereIniziale+len(numero)-1
    #stessa riga
    #carattere prima
    if(indexCarattereIniziale != 0 and isSimbolo(lines[indexRiga][indexCarattereIniziale-1])):
        return True
    #carattere dopo
    if(indexCarattereFinale+1 < len(lines[indexRiga]) and isSimbolo(lines[indexRiga][indexCarattereFinale+1])):
        return True
    
    #altre righe
    estremo1Caratteri=0 if indexCarattereIniziale==0 else indexCarattereIniziale-1
    estremo2Caratteri=indexCarattereFinale if indexCarattereFinale+1==len(lines[indexRiga]) else indexCarattereFinale+1
    
    #riga prima
    if(indexRiga != 0 and isThereSimboloInLista(lines[indexRiga-1][estremo1Caratteri:estremo2Caratteri+1])):
        return True
    #riga dopo
    if(indexRiga+1 < len(lines) and isThereSimboloInLista(lines[indexRiga+1][estremo1Caratteri:estremo2Caratteri+1])):
        return True
    return False
    
totale=0
for indexRiga, riga in enumerate(lines):
    buffer=""
    indexCarattereFinale = 0
    for carattere in riga:
        if carattere.isnumeric():
            buffer+=carattere
        elif buffer != "":
            totale+=int(buffer) if checkNumero(buffer, indexRiga, indexCarattereFinale-len(buffer)) else 0
            buffer = ""
        indexCarattereFinale+=1
    if buffer !="":
        totale+=int(buffer) if checkNumero(buffer, indexRiga, indexCarattereFinale-len(buffer)) else 0
print(totale)