def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
    
f = open("input.txt", "r")

result = 0

for line in f:
    low = 9999
    high = -1

    for c in line.split("\t"):
        if RepresentsInt(c):
            if low > int(c):
                low = int(c)
                print("New low: " + c)
            if high < int(c):
                high = int(c) 
                print("New high: " + c)
    result = result + (high - low)
    print(result)
    print("\n")

print(result)

f.close()
