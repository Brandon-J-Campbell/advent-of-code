f = open("input.txt", "r")

lines = []
instructions = []
stacks = []
mode = 0
numberOfColumns = -1

for line in f:
    if len(line.rstrip()) == 0:
        lastline = lines[len(lines)-1]
        numberOfColumns = int(lastline[len(lastline)-1])
        lines.pop()
        mode = 1
        continue
    
    if mode == 0:
        lines.append(line.rstrip())
    else:
        instructions.append(line.rstrip())

i = 0
while i < numberOfColumns:
    stacks.append([])
    i = i + 1


for line in lines:
    i = 0
    while i < numberOfColumns:
        index = i * 4 + 1
        if len(line) > index:
            if line[index] != " ":
                stacks[i].insert(0, line[index])
        i = i + 1

for instruction in instructions:
    arr = instruction.split(" ")
    i = int(arr[1])
    while i > 0:
        crate = stacks[int(arr[3])-1].pop()
        stacks[int(arr[5])-1].append(crate)
        i = i - 1
    
result = ""
for stack in stacks:
    result = result + stack[len(stack)-1]

print(result)

f.close()
