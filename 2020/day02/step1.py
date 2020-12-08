def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
    
def countChar(c, s):
    count = 0
    for i in range(len(s)):
        if (s[i] == c):
            count = count + 1
    return count

f = open("input.txt", "r")

result = 0
for line in f:
    lineArray = line.rstrip().split(":")
    password = lineArray[1]
    rulesArray = lineArray[0].rstrip().split(" ")
    letter = rulesArray[1]
    countArray = rulesArray[0].rstrip().split("-")
    minCount = int(countArray[0])
    maxCount = int(countArray[1])
    count = countChar(letter, password)

    if count >= minCount and count <= maxCount:
        result = result + 1

    

print(result)

f.close()
