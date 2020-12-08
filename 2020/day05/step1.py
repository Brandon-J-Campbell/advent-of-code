def countChar(c, s):
    count = 0
    for i in range(len(s)):
        if (s[i] == c):
            count = count + 1
    return count

f = open("input.txt", "r")

result = 0

for line in f:
    row = 0
    for i in range(7):
        if line[i] == "B":
            row = row + (2 ** (7 - (i + 1)))
        
    seat = 0
    for i in range(3):
        if line[i + 7] == "R":
            seat = seat + (2 ** (10 - (i + 8)))
    
    id = (row * 8) + seat
    
    if id > result:
        result = id
        
    print(line.rstrip() + ": row " + str(row) + ", column: " + str(seat) + ", seat ID: " + str(id))
        
print(result)

f.close()
