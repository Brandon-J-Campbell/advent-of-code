def containsShinyGold(bags, containsDict):
    if "shiny gold" in containsDict:
        return True
    
    isContained = False
    for bag in containsDict.keys():
        if bag not in bags:
            continue
        isContained = containsShinyGold(bags, bags[bag]["contains"])
        if isContained:
            break
    return isContained
    
f = open("input.txt", "r")

result = 0
bags = {}
stringsToRemove = [" bags", " bag", "."]

for line in f:
    bagArray = line.rstrip().split(" bags contain ")
    bag = bagArray[0]
    containsArray = bagArray[1].split(", ")
    bags[bag] = {}
    containsDict = {}
    for contains in containsArray:
        bagInfoArray = contains.split(" ", 1)
        bagInfo = bagInfoArray[1]
        for remove in stringsToRemove:
            bagInfo = bagInfo.replace(remove, "")
        containsDict[bagInfo] = bagInfoArray[0]
    bags[bag]["contains"] = containsDict
    
for bag in bags.keys():
    if containsShinyGold(bags, bags[bag]["contains"]):
        result = result + 1

print(result)
f.close()
