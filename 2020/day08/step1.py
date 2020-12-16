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

    return result

f = open("input.txt", "r")

instructions = []
for line in f:
    instructionArray = line.rstrip().split(" ")
    instructions.append(instructionArray)
    
print(isInfinite(instructions))
f.close()
