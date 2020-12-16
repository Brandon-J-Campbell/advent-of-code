def adjacentSeats(seatingChart, i, j):
    rv = []
    for row in range(i - 1, i + 2):
        if row >= 0 and row < len(seatingChart):
            for column in range(j - 1, j + 2):
                if column >= 0 and column < len(seatingChart[row]):
                    if row != i or column != j:
                        rv.append(seatingChart[row][column])
    return rv
    
def newValue(seatingChart, i, j):
    oldValue = seatingChart[i][j]
    seats = adjacentSeats(seatingChart, i, j)
    if oldValue == "L":
        if "#" not in seats:
            return "#"
    elif oldValue == "#":
        if seats.count("#") >= 4:
            return "L"
    
    return oldValue
    
def copyArray(seatingChart):
    newChart = []
    for i in range(len(seatingChart)):
        newRow = []
        for j in range(len(seatingChart[i])):
            newRow.append(seatingChart[i][j])
        newChart.append(newRow)
    return newChart

f = open("input.txt", "r")

seatingChart = []

row = 0
for line in f:
    line = line.rstrip()
    columns = []
    for i in range(len(line)):
        columns.append(line[i])
    seatingChart.append(columns)

notDone = True
while notDone:
    for i in range(len(seatingChart)):
        print(seatingChart[i])
    print("----")
    notDone = False
    newSeatingChart = copyArray(seatingChart)
    for i in range(len(seatingChart)):
        for j in range(len(seatingChart[i])):
            newSeatingChart[i][j] = newValue(seatingChart, i, j)
            if newSeatingChart[i][j] != seatingChart[i][j]:
                notDone = True
    seatingChart = copyArray(newSeatingChart)
    
result = 0
for i in range(len(seatingChart)):
    result = result + seatingChart[i].count("#")
    print(seatingChart[i])
print(result)
f.close()
