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

occurrences=0
for leftElement in left:
   total=0
   for rightElement in right:
      if(int(leftElement) == int(rightElement)):
         total +=1
   occurrences += total * int(leftElement)

print(occurrences)