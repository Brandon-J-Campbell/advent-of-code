def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
        
f = open("input.txt", "r")

memory = {}
mask = ""
instructions = []
for line in f:
    line = line.rstrip()
    if line[1] == "a":
        mask = line.split(" = ")[1]
        print(mask)
    else:
        instruction = []
        lineArray = line.split("] = ")
        instruction.append(lineArray[0].lstrip("mem["))
        instruction.append(str(bin(int(lineArray[1])))[2:])
        print(instruction[1])
        value = ""
        maskLength = len(mask) - 1
        for i in range(len(mask)):
            if mask[maskLength - i] == "X":
                if i < len(instruction[1]):
                    instrLength = len(instruction[1]) - 1
                    value = instruction[1][instrLength - i] + value
                else:
                    value = "0" + value
            else:
                value = mask[maskLength - i] + value
            
        memory[instruction[0]] = value

result = 0
for key in memory.keys():
    value = memory[key]
    valueLength = len(memory[key]) - 1
    memValue = 0
    for i in range(len(memory[key])):
        bit = value[valueLength - i]
        if bit == "1":
            memValue = memValue + (2**i)
    result = result + memValue
print(result)
f.close()
