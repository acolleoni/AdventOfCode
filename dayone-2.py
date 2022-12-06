import array

f = open("file.txt", "r")
lines = f.readlines()

i=0
elfi = [0]

for line in lines:
    if line.strip():
        elfi[i]=elfi[i]+int(line)
    else:
        i=i+1
        elfi.append(0)
f.close()

elfi.sort()

print((elfi[i]+elfi[i-1]+elfi[i-2]))