text = '''3   4
4   3
2   5
1   3
3   9
3   3'''
splitText = text.split("\n")

left=[]
right=[]
for element in splitText:
   left.append(element.split("   ")[0])
   right.append(element.split("   ")[1])

left.sort()
right.sort()

distances=[]
for index, leftElement in enumerate(left):
   distances.append(abs(int(leftElement)-int(right[index])))

total=0
for element in distances:
   total+=element

print(total)