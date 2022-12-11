def processPixel(row, cycle, x):
    if cycle >= x and cycle <= x+2:
        row.append("#")
    else:
        row.append(".")
    return row

f = open("input.txt", "r")

cycle = 1
x = 1
rows = []
row = ["."]

for line in f:
    line = line.rstrip()
    instr = line.split(" ")
    row = processPixel(row, cycle, x)       

    if instr[0] == "noop":
        cycle += 1
    elif instr[0] == "addx":
        cycle += 1
        
        if (cycle - 1) % 40 == 0:
            rows.append(row)
            row = ["."]
            cycle = 1

        row = processPixel(row, cycle, x)
        cycle += 1
        x += int(instr[1])

    if (cycle - 1) % 40 == 0:
        rows.append(row)
        row = ["."]
        cycle = 1

for row in rows:
    print(row)
    
f.close()

