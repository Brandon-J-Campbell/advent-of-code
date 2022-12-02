def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def evalTotal(highs, total):
    if total > highs[2]:
        highs[2] = total
    if total > highs[1]:
        highs[2] = highs[1]
        highs[1] = total
    if total > highs[0]:
        highs[1] = highs[0]
        highs[0] = total
    
    return highs

f = open("input.txt", "r")

highs = [0, 0, 0]
total = 0

for line in f:
    if RepresentsInt(line):
        total = total + int(line)
    else:
        highs = evalTotal(highs, total)
        total = 0

highs = evalTotal(highs, total)

print(highs[0] + highs[1] + highs[2])

f.close()

