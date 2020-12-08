def countChar(c, s):
    count = 0
    for i in range(len(s)):
        if (s[i] == c):
            count = count + 1
    return count
    
def treesHit(map, slopeX, slopeY):
    result = 0
    xPos = 0
    yPos = 0

    while yPos < len(map):
        line = map[yPos]
        if line[xPos] == "#":
            result = result + 1
        
        yPos = yPos + slopeY
        xPos = xPos + slopeX
        if xPos >= len(line):
            xPos = xPos - len(line)
    return result
    
f = open("input.txt", "r")

map = []
slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]

for line in f:
    lineArray = []
    for i in range(0, len(line) - 1):
        lineArray.append(line[i])
    map.append(lineArray)

result = 1
for slope in slopes:
    result = result * treesHit(map, slope[0], slope[1])
        
print(result)

f.close()
