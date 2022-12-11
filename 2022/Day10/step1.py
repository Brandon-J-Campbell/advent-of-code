f = open("input.txt", "r")

cycle = 1
x = 1
xValues = [0]

for line in f:
    line = line.rstrip()
    instr = line.split(" ")
    
    if instr[0] == "noop":
        xValues.append(x)
        cycle += 1
    elif instr[0] == "addx":
        xValues.append(x)
        xValues.append(x)
        x += int(instr[1])
        cycle += 2

i = 20
result = 0
while i < len(xValues):
    result += xValues[i] * i
    i += 40

print(result)
f.close()
