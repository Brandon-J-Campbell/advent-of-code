f = open("input.txt", "r")
input = f.read()
position = 0
buffer = ""
for c in input:
    buffer += c
    found = -1
    if len(buffer) > 3:
        string = buffer[len(buffer)-4:]
        for test in string:
            stringToTest = string.replace(test, '')
            if len(stringToTest) < 3:
                found = 0
        
        if found == -1:
            break
    position += 1
print(position + 1)

f.close()
