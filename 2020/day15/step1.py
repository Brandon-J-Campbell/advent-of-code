def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
        
f = open("input.txt", "r")

numbers = []
memory = {}
mask = ""
instructions = []
for line in f:
    line = line.rstrip()
    numbers = line.split(",")
    
lastNumber = -1
for i in range(0, 2020):
    if i < len(numbers):
        if i > 0:
            memory[lastNumber] = i
        lastNumber = numbers[i]
        continue
    oldNumber = lastNumber
    if lastNumber not in memory:
        numbers.append("0")
        lastNumber = "0"
    else:
        newNumber = str(i - memory[lastNumber])
        numbers.append(newNumber)
        lastNumber = newNumber
    memory[oldNumber] = i
        
print(numbers)
f.close()
