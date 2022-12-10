f = open("input.txt", "r")

PosX = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
PosY = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

visited = ["0,0"]

for line in f:
    line = line.rstrip()
    instr = line.split(" ")
    
    i = 0
    while i < int(instr[1]):
        front = 0
        back = 1
        if instr[0] == "R":
            PosX[front] += 1
        elif instr[0] == "U":
            PosY[front] += 1
        elif instr[0] == "L":
            PosX[front] -= 1
        elif instr[0] == "D":
            PosY[front] -= 1

        while back < len(PosX):
            movedX = PosX[front] - PosX[back]
            movedY = PosY[front] - PosY[back]

            if abs(movedX) > 1 or abs(movedY) > 1:
                if abs(movedX) > 1:
                    if movedX > 0:
                        PosX[back] += 1
                    else:
                        PosX[back] -= 1

                    if movedY != 0:
                        if movedY > 0:
                            PosY[back] += 1
                        elif movedY < 0:
                            PosY[back] -= 1
                else:
                    if movedY > 0:
                        PosY[back] += 1
                    else:
                        PosY[back] -= 1
    
                    if movedX > 0:
                        PosX[back] += 1
                    elif movedX < 0:
                        PosX[back] -= 1

            if back == len(PosX) - 1:
                strg = str(PosX[back]) + "," + str(PosY[back])
                if strg not in visited:
                    visited.append(strg)

            back += 1
            front += 1

        i += 1

print(len(visited))

f.close()

