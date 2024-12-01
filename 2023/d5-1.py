f = open("input5.txt", "r")
lines=f.readlines()
f.close()

class AlmanacMap:
    typeFrom=""
    typeTo=""
    mapString : str=""
    mapArray : list[str]=[]
    def __init__(self, typeFrom : str, typeTo : str):
        self.typeFrom=typeFrom
        self.typeTo=typeTo
        self.typeTo.replace(":","")
    def __str__(self):
        return self.typeFrom+" to "+self.typeTo+" map is "+str(self.mapArray)

class Seed:
    id=""
    characteristics : dict[str, int]={}
    def __init__(self,id : int):
        self.id=id
        self.characteristics={}
    def __str__(self):
        return str(self.id) + " " + str(self.characteristics)

seedList=[]
for seedLine in lines[0].replace("\n","").split(": ")[1].split(" "):
    seedList.append(Seed(int(seedLine)))

almanacMaps=[]
inMap=False
for line in lines[1::]:
    if(line.find(":") > 0):
        almanacMaps.append(AlmanacMap(line.split(" ")[0].split("-")[0], line.split(" ")[0].split("-")[2]))
        inMap=True
    elif(inMap):
        almanacMaps[len(almanacMaps)-1].mapString+=line

for map in almanacMaps:
    map.mapArray=list(filter(None, map.mapString.split("\n")))

for map in almanacMaps:
    for mapLine in map.mapArray:

        destinationStart=int(mapLine.split(" ")[0])
        sourceStart=int(mapLine.split(" ")[1])
        length=int(mapLine.split(" ")[2])
    
        for index, seed in enumerate(seedList):
            if(map.typeFrom=="seed"):
                if(int(seed.id) >= sourceStart and int(seed.id) < (sourceStart+length)):
                    seedList[index].characteristics[map.typeTo]=destinationStart+(seed.id-sourceStart)
            elif(int(seed.characteristics[map.typeFrom]) >= sourceStart and int(seed.characteristics[map.typeFrom]) < (sourceStart+length)):
                seedList[index].characteristics[map.typeTo]=destinationStart+(seed.characteristics[map.typeFrom]-sourceStart)
    if(map.typeFrom!="seed"):
        for index, seed in enumerate(seedList):
            try:
                testVariable=seed.characteristics[map.typeTo]
            except:
                seedList[index].characteristics[map.typeTo]=seedList[index].characteristics[map.typeFrom]
    if (map.typeFrom == "seed"):
        for index, seed in enumerate(seedList):
            try:
                testVariable = seed.characteristics["soil"]
            except:
                seedList[index].characteristics["soil"] = seed.id

print(min(seedList, key=lambda x: x.characteristics["location"]).characteristics["location"])