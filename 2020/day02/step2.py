f = open("input.txt", "r")

result = 0
for line in f:
    lineArray = line.rstrip().split(":")
    password = lineArray[1]
    rulesArray = lineArray[0].rstrip().split(" ")
    letter = rulesArray[1]
    posArray = rulesArray[0].rstrip().split("-")
    pos1 = int(posArray[0])
    pos2 = int(posArray[1])

    if (password[pos1] == letter) ^ (password[pos2] == letter):
        result = result + 1

    

print(result)

f.close()

