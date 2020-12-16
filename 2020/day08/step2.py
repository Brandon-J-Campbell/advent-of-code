def isInfinite(instructions):
    result = 0
    i = 0
    tracker = {}
    while i not in tracker and i < len(instructions):
        tracker[i] = 1
        instruction = instructions[i]
        if instruction[0] == "acc":
            result = result + int(instruction[1])
            i = i + 1
        elif instruction[0] == "jmp":
            i = i + int(instruction[1])
        elif instruction[0] == "nop":
            i = i + 1
    
    if i < len(instructions):
        return -1
    else:
        return result

f = open("input.txt", "r")

instructions = []
for line in f:
    instructionArray = line.rstrip().split(" ")
    instructions.append(instructionArray)
    
nopIndex = -1
oldInstruction = ""
working = True
while working:
    if nopIndex > -1:
        instructions[nopIndex][0] = oldInstruction
    nopIndex = nopIndex + 1
    for i in range(nopIndex, len(instructions)):
        if instructions[i][0] == "nop" or instructions[i][0] == "jmp":
            nopIndex = i
            oldInstruction = instructions[i][0]
            if instructions[i][0] == "nop":
                instructions[i][0] = "jmp"
            else:
                instructions[i][0] = "nop"
            break

    result = isInfinite(instructions)
    if result > -1:
        print(result)
        working = False

f.close()
