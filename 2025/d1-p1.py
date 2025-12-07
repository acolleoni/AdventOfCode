file = open('input1.txt', 'r')
lines = file.readlines()
position=50
password=0
for line in lines:
   movement=int(line[1:])
   if line[0]=='L':
      position = (position-movement)%100
   else:
      position = (position+movement)%100
   if position == 0:
      password = password+1
print(password)