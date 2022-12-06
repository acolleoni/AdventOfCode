import array

f = open("file4.txt", "r")
lines = f.readlines()
f.close()

i=0
for line in lines:
    separata=line.replace('\n', '')
    separata=separata.split(",")
    separata[0]=separata[0].split("-")
    separata[1]=separata[1].split("-")
    intera=[[0,0],[0,0]]
    intera[0][0]=int(separata[0][0])
    intera[0][1]=int(separata[0][1])
    intera[1][0]=int(separata[1][0])
    intera[1][1]=int(separata[1][1])
    print(separata)
    
    if ((intera[0][0] <= intera[1][0] and intera[0][1] >= intera[1][1]) or (intera[0][0] >= intera[1][0] and intera[0][1] <= intera[1][1])):
        i=i+1
        print("<- here")

print("\n")
print(i)