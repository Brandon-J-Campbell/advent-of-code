def countBags(bags, bag, count):
    if len(bag["contains"]) == 0:
        return count
    
    total = count
    for containedBag in bag["contains"].keys():
        bagCount = countBags(bags, bags[containedBag], bag["contains"][containedBag])
        total = total + (bagCount * count)
        
    return total
    
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
        
        if bagInfo != "other":
            containsDict[bagInfo] = int(bagInfoArray[0])
            
    bags[bag]["contains"] = containsDict
    
bag = bags["shiny gold"]
result = countBags(bags, bag, 1) - 1
print(result)
f.close()
