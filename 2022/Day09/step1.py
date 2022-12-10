f = open("input.txt", "r")

hPosX = 0
hPosY = 0
tPosX = 0
tPosY = 0

visited = [str(tPosX) + "," + str(tPosY)]

for line in f:
    line = line.rstrip()
    instr = line.split(" ")
    
    i = 0
    while i < int(instr[1]):
        if instr[0] == "R":
            hPosX += 1
        elif instr[0] == "U":
            hPosY += 1
        elif instr[0] == "L":
            hPosX -= 1
        elif instr[0] == "D":
            hPosY -= 1

        movedX = hPosX - tPosX
        movedY = hPosY - tPosY

        if abs(movedX) > 1 or abs(movedY) > 1:
            if abs(movedX) > 1:
                if movedX > 0:
                    tPosX += 1
                else:
                    tPosX -= 1

                if movedY != 0:
                    if movedY > 0:
                        tPosY += 1
                    elif movedY < 0:
                        tPosY -= 1
            else:
                if movedY > 0:
                    tPosY += 1
                else:
                    tPosY -= 1
    
                if movedX > 0:
                    tPosX += 1
                elif movedX < 0:
                    tPosX -= 1

        strg = str(tPosX) + "," + str(tPosY)
        if strg not in visited:
            visited.append(strg)

        i += 1

print(len(visited))

f.close()
