f = open("input.txt", "r")

direction = "E"
degrees = 90
currentPosition = [0, 0]
waypointPosition = [10, 1]

for line in f:
    line = line.rstrip()
    instruction = line[0]
    count = int(line.lstrip(instruction))
    
    if instruction == "N":
        waypointPosition[1] = waypointPosition[1] + count
    elif instruction == "S":
        waypointPosition[1] = waypointPosition[1] - count
    elif instruction == "E":
        waypointPosition[0] = waypointPosition[0] + count
    elif instruction == "W":
        waypointPosition[0] = waypointPosition[0] - count
    elif instruction == "F":
        currentPosition[0] = currentPosition[0] + (waypointPosition[0] * count)
        currentPosition[1] = currentPosition[1] + (waypointPosition[1] * count)
    elif instruction == "L" or instruction == "R":
        if count == 180:
            waypointPosition[0] = waypointPosition[0] * -1
            waypointPosition[1] = waypointPosition[1] * -1
            continue
        
        if count == 270:
            count = 90
            if instruction == "L":
                instruction = "R"
            else:
                instruction = "L"
                
        #figure this out
        newWaypointPosition = [0,0]
        if instruction == "L":
            newWaypointPosition[0] = waypointPosition[1] * -1
            newWaypointPosition[1] = waypointPosition[0]
#            if waypointPosition[0] >= 0 && waypointPosition[1] >= 0:
#                waypointPosition[0] = waypointPosition[1] * -1
#                waypointPosition[1] = waypointPosition[0]
#            elif waypointPosition[0] < 0 && waypointPosition[1] >= 0:
#                waypointPosition[0] = waypointPosition[1] * -1
#                waypointPosition[1] = waypointPosition[0]
#            elif waypointPosition[0] < 0 && waypointPosition[1] < 0:
#                waypointPosition[0] = waypointPosition[1] * -1
#                waypointPosition[1] = waypointPosition[0]
#            else:
#                waypointPosition[0] = waypointPosition[1] * -1
#                waypointPosition[1] = waypointPosition[0]
        else:
            newWaypointPosition[0] = waypointPosition[1]
            newWaypointPosition[1] = waypointPosition[0] * -1
        waypointPosition = newWaypointPosition
        
    print("Current Position: ")
    print(currentPosition)
    print("Current Waypoint: ")
    print(waypointPosition)
            
print(currentPosition)
print(abs(currentPosition[0]) + abs(currentPosition[1]))
f.close()
