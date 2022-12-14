f = open("file5.txt", "r")
lines = f.readlines()
f.close()

i=0
b=0
schemino = [""]
mosse =[""]

for line in lines:
    if not line.strip():
        b=1
        i=0
    elif not b :
        schemino[i]=line.replace('\n', '')
        i=i+1
        schemino.append("")
    else:
        mosse[i]=line.replace('\n', '')
        i=i+1
        mosse.append("")

schemino.remove('')
mosse.remove('')


#parsing delle mosse - lo faccio prima perche sembra meno impossibile
#movimento di X cubbett da Y a Z
lavoro=[""]
lavorodue=[""]
i=0
for mossa in mosse:
    lavoro[i]=mossa.replace('move ', '')
    lavoro[i]=lavoro[i].split(" from ")
    lavoro[i][1]=lavoro[i][1].split(" to ")
    i=i+1
    lavoro.append("")
lavoro.remove('')

movimento=[]
for lavori in lavoro:
    movimento.append([int(lavori[0]), int(lavori[1][0]), int(lavori[1][1])])

#parsing dello schemino - aiuto
#1-trovo quante sono le colonne
rigafinale=schemino[(len(schemino)-1)]
colonne=0
for caratteri in rigafinale:
    if caratteri != " ":
        if int(caratteri) > colonne:
            colonne=int(caratteri)

#2-trovo quante sono le righe
righe=len(schemino)-1

#3-leggo le righe una alla volta
schemino.pop((len(schemino)-1))
j=0 
k=1
i=0
mappa=[]
for riga in schemino:
    mappa.append([])
    while(j<colonne):
        mappa[i].append(riga[k])
        k=k+4
        j=j+1
    k=1
    j=0
    i=i+1


#inverto la matrice
nuovamappa=[]
i=len(mappa)-1
j=0
k=0
while(j<colonne):
    nuovamappa.append([])
    while(i>=0):
        nuovamappa[k].append(mappa[i][j])
        i=i-1
    j=j+1
    k=k+1
    i=len(mappa)-1

#tolgo gli spazi vuoti
def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]
mappasenzaspazi=[]
for elemento in nuovamappa:
    mappasenzaspazi.append(remove_values_from_list(elemento, " "))
           


#sposto secondo le indicazioni
for movimenti in movimento:
    quanticubbett=movimenti[0]
    da=movimenti[1]-1
    a=movimenti[2]-1
    fine=len(mappasenzaspazi[da])
    
    i=1
    j=fine-quanticubbett
    while(i<=quanticubbett):
        mappasenzaspazi[a].append(mappasenzaspazi[da][j])
        i=i+1
        j=j+1
    i=1
    while(i<=quanticubbett):
        mappasenzaspazi[da].pop(len(mappasenzaspazi[da])-1)
        i=i+1

#stampo cosa sta in cima a ogni fila
for fila in mappasenzaspazi:
    print (fila[len(fila)-1])