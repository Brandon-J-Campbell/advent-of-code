f = open("input.txt", "r")

direction = "E"
degrees = 90
currentPosition = [0, 0]

for line in f:
    line = line.rstrip()
    instruction = line[0]
    count = int(line.lstrip(instruction))
    if instruction == "F":
        instruction = direction
    
    if instruction == "N":
        currentPosition[1] = currentPosition[1] + count
    elif instruction == "S":
        currentPosition[1] = currentPosition[1] - count
    elif instruction == "E":
        currentPosition[0] = currentPosition[0] + count
    elif instruction == "W":
        currentPosition[0] = currentPosition[0] - count
    elif instruction == "L" or instruction == "R":
        if instruction == "L":
            degrees = degrees - count
            if degrees < 0:
                degrees = degrees + 360
        else:
            degrees = degrees + count
            if degrees > 359:
                degrees = degrees - 360
        
        if degrees == 0:
            direction = "N"
        elif degrees == 90:
            direction = "E"
        elif degrees == 180:
            direction = "S"
        else:
            direction = "W"
            
print(currentPosition)
print(abs(currentPosition[0]) + abs(currentPosition[1]))
f.close()
