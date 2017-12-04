def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
    
f = open("input.txt", "r")

input = f.read()

result = 0
first = -1
last = -1
for c in input:
    if RepresentsInt(c):
        if first == -1:
            first = int(c)

        if int(c) == last:
            result = result + last

        last = int(c)

if last == first:
    result = result + last
        
print(result)

f.close()
