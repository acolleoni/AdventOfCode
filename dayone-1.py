import array

f = open("file.txt", "r")
lines = f.readlines()

i=0
elfi = [0]

for line in lines:    
    if line.strip() :
        elfi[i]=elfi[i]+int(line)
    else:
        i=i+1
        elfi.append(0)
f.close()
print(elfi)

ris=elfi[0]
for elfo in elfi:
    if elfo >= ris:
        ris = elfo
print(ris)