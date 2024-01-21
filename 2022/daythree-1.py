import array

f = open("file3.txt", "r")
lines = f.readlines()

i=0
j=0
k=0
primameta=[""]
secondameta=[""]
lettere=[""]

for line in lines:
    while i < (int(len(line)/2)):
        primameta[j]=primameta[j]+line[i]
        i=i+1
    while i < (int(len(line))):
        if(line[i]=="\n"):
            break
        else:
            secondameta[j]=secondameta[j]+line[i]
        i=i+1
    j=j+1
    primameta.append("")
    secondameta.append("")
    i=0
    k=k+1
print(primameta)
print(secondameta)
f.close()

i=0
while(i<len(primameta)):
    for carattere in primameta[i]:
        for carattera in secondameta[i]:
            if carattere==carattera:
                lettere[i]=carattere
                lettere.append("")
    i=i+1
print(lettere)

ris=0
for lettera in lettere:
    if(lettera != ""):
        if (ord(lettera)<97):
            print (ord(lettera)-64+26)
            ris+=ord(lettera)-64+26
        else:
            print (ord(lettera)-96)
            ris+=ord(lettera)-96
print("\n")
print(ris)

