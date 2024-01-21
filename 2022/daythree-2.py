import array

f = open("file3.txt", "r")
lines = f.readlines()

lettere=[""]

i=0
k=0

while(i<((len(lines))-2)):
    for carattere in lines[i]:
        for carattera in lines[i+1]:
            for caratteru in lines[i+2]:
                if carattere != "\n":
                    if carattere==carattera==caratteru:
                        lettere[k]=carattere
                        lettere.append("")
    i=i+3
    k=k+1
f.close()

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