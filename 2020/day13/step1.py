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
    
shortestWait = 999999999
busId = 0
for bus in busses:
    if RepresentsInt(bus):
        modulo = timestamp % int(bus)
        waittime = int(bus) - modulo
        if waittime < shortestWait:
            shortestWait = waittime
            busId = int(bus)
            
print(busId * shortestWait)
f.close()
