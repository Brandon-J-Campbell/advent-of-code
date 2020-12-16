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
    else:
        instruction = []
        lineArray = line.split("] = ")
        instruction.append(str(bin(int(lineArray[0].lstrip("mem["))))[2:])
        instruction.append(lineArray[1])
        value = instruction[1]
        
        memAddress = instruction[0]
        memAddressMax = len(memAddress) - 1
        memValues = [""]
        maskMax = len(mask) - 1
        newAddress = ""
        maskLength = len(mask) - 1
        for i in range(len(mask)):
            if mask[maskLength - i] == "0":
                if i < len(memAddress):
                    memLength = len(memAddress) - 1
                    newAddress = memAddress[memLength - i] + newAddress
                else:
                    newAddress = "0" + newAddress
            elif mask[maskLength - i] == "1":
                newAddress = "1" + newAddress
            else:
                newAddress = "X" + newAddress
                
        memAddress = newAddress
        for i in range(len(memAddress)):
            if memAddress[i] == "0" or memAddress[i] == "1":
                for j in range(len(memValues)):
                    memValues[j] = memValues[j] + memAddress[i]
            else:
                newMem = []
                for mem in memValues:
                    newMem.append(mem + "0")
                    newMem.append(mem + "1")
                memValues = newMem
        for mem in memValues:
            address = mem.rjust(36, '0')
            memory[address] = value
        

result = 0
for key in memory.keys():
    result = result + int(memory[key])

print(result)
f.close()
