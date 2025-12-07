file = open('input1.txt', 'r')
lines = file.readlines()
position=50
password=0
for line in lines:
   movement=int(line[1:])
   oldposition = position
   if movement > 99:
       password = password + int(movement/100)
       movement = movement%100
   if line[0]=='L':
      position = (position-movement)%100
      if (position > oldposition and oldposition != 0) or position == 0:
          password = password + 1
   else:
      position = (position+movement)%100
      if (position < oldposition and oldposition != 0) or position == 0:
          password = password + 1
print(password)