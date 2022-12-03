f = open("input.txt", "r")

total = 0
i = 0

strings = []

for line in f:
    line = line.rstrip()
        
    if i == 2:
        for c in line:
            if strings[0].__contains__(c) and strings[1].__contains__(c):
                value = ord(c)
                if value <= 90:
                    value = value - 38
                else:
                    value = value - 96
                total = total + value
                break

        strings = []
        i = 0
    else:
        strings.append(line)
        i = i + 1

print(total)

f.close()

