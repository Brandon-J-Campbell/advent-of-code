def countChar(c, s):
    count = 0
    for i in range(len(s)):
        if (s[i] == c):
            count = count + 1
    return count

f = open("input.txt", "r")

result = 0
map = []
for line in f:
    lineArray = []
    for i in range(0, len(line) - 1):
        lineArray.append(line[i])
    map.append(lineArray)
    
xPos = 0
yPos = 0

while yPos < len(map):
    line = map[yPos]
    if line[xPos] == "#":
        result = result + 1
    
    yPos = yPos + 1
    xPos = xPos + 3
    if xPos >= len(line):
        xPos = xPos - len(line)
        
print(result)

f.close()
