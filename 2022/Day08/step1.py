def check(woods, i, j):
    print("i: " + str(i) + ", j: " + str(j) + ", height: " + str(woods[i][j]))
    row = woods[i]
    height = row[j]

    visible = 1
    checki = i - 1
    while checki >= 0:
        if woods[checki][j] >= height:
            visible = 0
            break
        checki -= 1

    if visible > 0:
        return visible

    visible = 1
    checki = i + 1
    while checki < len(woods):
        if woods[checki][j] >= height:
            visible = 0
            break
        checki += 1

    if visible > 0:
        return visible

    visible = 1
    checkj = j - 1
    while checkj >= 0:
        if woods[i][checkj] >= height:
            visible = 0
            break
        checkj -= 1

    if visible > 0:
        return visible
    
    visible = 1
    checkj = j + 1
    while checkj < len(woods[i]):
        if woods[i][checkj] >= height:
            visible = 0
            break
        checkj += 1
        
    return visible

f = open("input.txt", "r")

woods = []
for line in f:
    line = line.rstrip()
    row = []
    for c in line:
        row.append(int(c))
    woods.append(row)

visible = 0
i = 0
while i < len(woods):
    j = 0
    while j < len(woods[i]):
        if i == 0 or j == 0 or i == len(woods)-1 or j == len(woods[i])-1:
            visible += 1
        elif check(woods, i, j) == 1:
            print("Visible")
            visible += 1
        j += 1
    i += 1

print(visible)

f.close()
