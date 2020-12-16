def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
        
f = open("input.txt", "r")

timestamp = 0
lineNumber = 0
busses = []
for line in f:
    line = line.rstrip()
    if lineNumber == 0:
        timestamp = int(line)
    else:
        busses = line.split(",")
    lineNumber = lineNumber + 1
    
keepRunning = True
i = 0
startingTimestamp = 487905974205100
while keepRunning:
    bus = busses[i]
    if RepresentsInt(bus):
        if (startingTimestamp + i) % int(bus) != 0:
            startingTimestamp = startingTimestamp + 1
            print(startingTimestamp)
            i = 0
            continue
        else:
            i = i + 1
            if i == len(busses):
                keepRunning = False
    else:
        i = i + 1
        
print(startingTimestamp)
f.close()
