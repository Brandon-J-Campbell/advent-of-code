def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
    
f = open("input.txt", "r")

high = 0
total = 0

for line in f:
    if RepresentsInt(line):
        total = total + int(line)
    else:
        if total > high:
            high = total
        total = 0		

if total > high:
    high = total

print(high)

f.close()
