def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
    
f = open("input.txt", "r")

result = 0

array = []

for line in f:
    print(line.rstrip())
    if RepresentsInt(line.rstrip()):
        array.append(int(line.rstrip()))

i = 0

print(len(array))
while i >= 0 and i < len(array):
    result = result + 1
    old = i
    i = i + array[i]
    if array[old] >= 3:
        array[old] = array[old] - 1
    else:
        array[old] = array[old] + 1

print(result)

f.close()
