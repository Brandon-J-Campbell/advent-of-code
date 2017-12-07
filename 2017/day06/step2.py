def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
    
def canGet(dict, x):
    try:
        value = dict[x]
        return True
    except:
        return False

def getStringKey(array):
    stringKey = ""
    for value in array:
        if len(stringKey) > 0:
            stringKey = stringKey + ","
        stringKey = stringKey + str(value)

    return stringKey

f = open("input.txt", "r")

result = 0

input = f.read()
dataArray = []

highIndex = 0
highValue = 0
i = 0

for c in input.split("\t"):
    if RepresentsInt(c):
        value = int(c)
        dataArray.append(value)
        if value > highValue:
            highIndex = i
            highValue = value
        i = i + 1

snapshots = { }

while not canGet(snapshots, getStringKey(dataArray)):
    print(dataArray)
    snapshots[getStringKey(dataArray)] = result
    print("High value: " + str(highValue) + ", high index: " + str(highIndex))
    count = dataArray[highIndex]
    dataArray[highIndex] = 0


    index = 0
    if highIndex + 1 < len(dataArray):
        index = highIndex + 1

    while count > 0:
        print("Current index: " + str(index) + ", highValue: " + str(highValue))
        dataArray[index] = dataArray[index] + 1
       
        if index + 1 < len(dataArray):
            index = index + 1
        else:
            index = 0

        count = count - 1

    highValue = 0
    highIndex = 0
    i = 0

    for value in dataArray:
        if dataArray[i] > highValue:
            highIndex = i
            highValue = dataArray[i]
        i = i + 1

    result = result + 1

print(dataArray)
print(result - snapshots[getStringKey(dataArray)])

f.close()
