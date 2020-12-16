def adjacentSeats(seatingChart, i, j):
    rv = []
    print("i: " + str(i) + ", j: " + str(j) + ", Current: " + seatingChart[i][j])
    for row in range(-1, 2):
        for column in range(-1, 2):
#            print("Row: " + str(row) + ", Column: " + str(column))
            currentX = i + row
            currentY = j + column
            if row != 0 or column != 0:
#                print("CurrentX: " + str(currentX) + ", CurrentY: " + str(currentY))
                while currentX >= 0 and currentX < len(seatingChart) and currentY >= 0 and currentY < len(seatingChart[i]):
                    if seatingChart[currentX][currentY] == "#" or seatingChart[currentX][currentY] == "L":
                        rv.append(seatingChart[currentX][currentY])
                        break
                    currentX = currentX + row
                    currentY = currentY + column
#                    print("CurrentX: " + str(currentX) + ", CurrentY: " + str(currentY))
    return rv
    
def newValue(seatingChart, i, j):
    oldValue = seatingChart[i][j]
    seats = adjacentSeats(seatingChart, i, j)
    if oldValue == "L":
        if "#" not in seats:
#            print("OldValue: " + str(oldValue) + ", i: " + str(i) + ", j: " + str(j))
#            print(seats)
            return "#"
    elif oldValue == "#":
        if seats.count("#") >= 5:
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
