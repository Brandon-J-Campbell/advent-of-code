from sys import argv
import math

def box(i):
    odd = int(math.sqrt(i - 1))
    if odd % 2 == 0:
        odd = odd - 1
    box = (odd + 1) / 2
    return box

def d(i):
    start = (odd ** 2) + box
    d = 0

    if input < start:
        d = start - input
    else:
        old = start
        while start < input:
            old = start
            start = start + (box * 2)
        d = min(start - input, input - old)
    return d

def get(dict, x, y):
    try:
        value = dict[x, y]
        print("Found " + str(value) + " at " + str(x) + ", " + str(y))
        return True
    except:
        return False

result = 1
input = int(argv[1])

dict = { (0, 0): 1}
i = 2
level = 1
position = 1, 0
direction = "up"

while result < input:
    level = box(i)
    print("Level: " + str(level)) 
    value = 0
    if get(dict, position[0] + 1, position[1]):
        value = value + dict[position[0] + 1, position[1]]
    
    if get(dict, position[0] + 1, position[1] + 1):
        value = value + dict[position[0] + 1, position[1] + 1]
    
    if get(dict, position[0], position[1] + 1):
        value = value + dict[position[0], position[1] + 1]

    if get(dict, position[0] - 1, position[1] + 1):
        value = value + dict[position[0] - 1, position[1] + 1]

    if get(dict, position[0] - 1, position[1]):
        value = value + dict[position[0] - 1, position[1]]

    if get(dict, position[0] - 1, position[1] - 1):
        value = value + dict[position[0] - 1, position[1] - 1]

    if get(dict, position[0], position[1] - 1):
        value = value + dict[position[0], position[1] - 1]

    if get(dict, position[0] + 1, position[1] - 1):
        value = value + dict[position[0] + 1, position[1] - 1]

    dict[position] = value
    i = i + 1
    result = value
    print(result)

    if direction == "up":
        if position[1] + 1 <= level:
            position = position[0], position[1] + 1
        else:
            direction = "left"

    if direction == "left":
        if abs(position[0] - 1) <= level:
            position = position[0] - 1, position[1]
        else:
            direction = "down"

    if direction == "down":
        if abs(position[1] - 1) <= level:
            position = position[0], position[1] - 1
        else:
            direction = "right"

    if direction == "right":
        if position[0] + 1 <= level:
            position = position[0] + 1, position[1]
        else:
            direction = "up"
            position = position[0] + 1, position[1]
    print("Next position: " + str(position[0]) + ", " + str(position[1]))

print(result)

