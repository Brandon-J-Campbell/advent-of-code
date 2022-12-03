f = open("input.txt", "r")

total = 0

for line in f:
    line = line.rstrip()
    mid = len(line) // 2
    first = line[:mid]
    last = line[mid:]
    for c in first:
        if last.__contains__(c):
            value = ord(c)
            if value <= 90:
                value = value - 38
            else:
                value = value - 96
            total = total + value
            break
print(total)

f.close()
