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
    
    # if ((intera[0][0] <= intera[1][0] and intera[0][1] >= intera[1][0]) or (intera[0][0] >= intera[1][0] and intera[0][1] >= intera[1][0])):
        # i=i+1
    # else:
        # print("<- not here")
        
    n=intera[0][0]
    b=0
    while n<=intera[0][1]:
        if ((n >= intera[1][0] and n <= intera[1][1])):
            b=1
        n=n+1
    if b:
        i=i+1
    else:
        print("<- not here")

print("\n")
print(i)