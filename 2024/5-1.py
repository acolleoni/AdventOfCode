f = open("input5.txt", "r")
lines = f.readlines()
f.close()

def findRule(page1, page2, rules):
    for rule in rules:
        if rule == (page1, page2) or rule == (page2, page1):
            return rule
    return (-1,-1)

rules=[]
queue=[]
inRules=True
for line in lines:
    if line == "\n":
        inRules=False
        continue
    if inRules:
        rules.append((line.strip().split("|")[0],line.strip().split("|")[1]))
    else:
        queue.append(line.strip().split(","))

validDocuments=[]
for document in queue:
    validDocument = True
    for index in range(len(document)-1):
        rule = findRule(document[index], document[index+1], rules)
        if rule == (-1,-1):
            continue
        if not rule[0]==document[index]:
            validDocument = False
    if validDocument:
        validDocuments.append(document)

solution=0
for document in validDocuments:
    solution += int(document[int(len(document)/2)])

print(solution)