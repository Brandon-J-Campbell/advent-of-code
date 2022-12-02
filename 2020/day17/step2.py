def countActive(pocket, key):
    activeCount = 0
    dimensions = key.split(",")
    originX = int(dimensions[0])
    for x in range(originX - 1, originX + 2):
        originY = int(dimensions[1])
        for y in range(originY - 1, originY + 2):
            originZ = int(dimensions[2])
            for z in range(originZ - 1, originZ + 2):
                originW = int(dimensions[3])
                for w in range(originW - 1, originW + 2):
                    lookup = str(x) + "," + str(y) + "," + str(z) + "," + str(w)
                    if lookup == key:
                        continue
                    
                    if lookup in pocket:
                        if pocket[lookup] == "#":
                            activeCount = activeCount + 1
    return activeCount
                        
f = open("input.txt", "r")

pocket = {}

lines = len(f.readlines())
y = (lines / 2 - lines) + 1

f.close()
f = open("input.txt", "r")

minX = 0
maxX = 0
minY = 0
maxY = 0
minZ = 0
maxZ = 0
minW = 0
maxW = 0

minY = min(minY, y)
maxY = max(maxY, y)

for line in f:
    line = line.rstrip()
    x = (len(line) / 2 - len(line)) + 1
    minX = min(minX, x)
    maxX = max(maxX, x)
    
    dimensions = ""
    for i in range(len(line)):
        dimensions = str(x) + "," + str(y) + ",0,0"
        pocket[dimensions] = line[i]
        x = x + 1
        minX = min(minX, x)
        maxX = max(maxX, x)
    
    y = y + 1
    minY = min(minY, y)
    maxY = max(maxY, y)
        
for i in range(6):
    newPocket = {}
    newMinX = 0
    newMaxX = 0
    newMinY = 0
    newMaxY = 0
    newMinZ = 0
    newMaxZ = 0
    newMinW = 0
    newMaxW = 0
    for x in range(minX - 1, maxX + 2):
        newMinX = min(newMinX, x)
        newMaxX = max(newMaxX, x)
        for y in range(minY - 1, maxY + 2):
            newMinY = min(newMinY, y)
            newMaxY = max(newMaxY, y)
            for z in range(minZ - 1, maxZ + 2):
                newMinZ = min(newMinZ, z)
                newMaxZ = max(newMaxZ, z)
                for w in range(minW - 1, maxW + 2):
                    newMinW = min(newMinW, w)
                    newMaxW = max(newMaxW, w)
                    key = str(x) + "," + str(y) + "," + str(z) + "," + str(w)
                    activeCount = countActive(pocket, key)
                    keyActive = False
                    if key in pocket:
                        keyActive = pocket[key] == "#"
                    print("Key: " + key + ", active: " + str(keyActive) + ", count: " + str(activeCount))
                    
                    if keyActive:
                        if (activeCount == 2 or activeCount == 3):
                            newPocket[key] = "#"
                            continue
                        else:
                            newPocket[key] = "."
                            continue
                        
                    if not keyActive and activeCount == 3:
                        newPocket[key] = "#"
                    else:
                        newPocket[key] = "."
        
    pocket = newPocket
    minX = newMinX
    maxX = newMaxX
    minY = newMinY
    maxY = newMaxY
    minZ = newMinZ
    maxZ = newMaxZ
    minW = newMinW
    maxW = newMaxW
    
#print(pocket)
count = 0
for key in pocket:
    if pocket[key] == "#":
        count = count + 1
        
print(count)
f.close()
