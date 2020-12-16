def hasNumberMatch(numbers, start, preamble):
    startIndex = max(start - 25, 0)
    stopIndex = min(startIndex + 25, start)
    print("Find: " + str(numbers[start]) + ", StartIndex: " + str(startIndex) + ", StopIndex: " + str(stopIndex))
    for i in range(startIndex, stopIndex):
        count = 0
        for j in range(i + 1, stopIndex):
            if numbers[i] + numbers[j] == numbers[start]:
                return True
    return False
    
f = open("input.txt", "r")

preamble = 25

numbers = []
for line in f:
    number = int(line.rstrip())
    numbers.append(number)

start = preamble
while True:
    if not hasNumberMatch(numbers, start, preamble):
        print(numbers[start])
        break
    start = start + 1
        
f.close()
