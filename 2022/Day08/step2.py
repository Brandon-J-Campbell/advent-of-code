def check(woods, i, j):
    print("i: " + str(i) + ", j: " + str(j) + ", height: " + str(woods[i][j]))
    row = woods[i]
    height = row[j]

    
    checki = i - 1
    up = 0
    while checki >= 0:
        up += 1
        if woods[checki][j] >= height:
            break
        checki -= 1

    checki = i + 1
    down = 0
    while checki < len(woods):
        down += 1
        if woods[checki][j] >= height:
            break
        checki += 1

    checkj = j - 1
    left = 0
    while checkj >= 0:
        left += 1
        if woods[i][checkj] >= height:
            break
        checkj -= 1

    checkj = j + 1
    right = 0
    while checkj < len(woods[i]):
        right += 1
        if woods[i][checkj] >= height:
            break
        checkj += 1
    print("Up: " + str(up) + ", Left: " + str(left) + ", Right: " + str(right) + ", Down " + str(down))
    return left * right * up * down

f = open("input.txt", "r")

woods = []
for line in f:
    line = line.rstrip()
    row = []
    for c in line:
        row.append(int(c))
    woods.append(row)

score = 0
i = 0
while i < len(woods):
    j = 0
    while j < len(woods[i]):
        total = check(woods, i, j)
        if total > score:
            score = total
        j += 1
    i += 1

print(score)

f.close()

