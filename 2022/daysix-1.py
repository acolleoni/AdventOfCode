f = open("file6.txt", "r")
testo=f.read()
f.close()

i=3
while(i<(len(testo)-1)):
    b=0
    j=0
    while(j<=3):
        k=0
        while(k<=3):
            if((i-k)!=(i-j)):
                if(testo[i-k]==testo[i-j]):
                    b+=1
                print(testo[i-k]+" "+testo[i-j] + " " +str(b))
            k=k+1
        j=j+1
    print("fine ciclo")
    if b==0:
        print(i+1)
        break
    i=i+1