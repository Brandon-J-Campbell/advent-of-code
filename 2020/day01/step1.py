def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
    
f = open("input.txt", "r")

inputs = []
for line in f:
    if RepresentsInt(line):
        inputs.append(int(line))

i = 1
result = 0
first = -1
second = -1

for a in inputs:
    first = a
    for j in range(i, len(inputs) - 1):
        if first + inputs[j] == 2020:
            second = inputs[j]
            break
    
    if second > -1:
        break

    i = i + 1

print(first * second)

f.close()
