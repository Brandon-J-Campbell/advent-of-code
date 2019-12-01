def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
    
f = open("input.txt", "r")

result = 0
for line in f:
    if RepresentsInt(line):
        result = result + int(line)

print(result)

f.close()
