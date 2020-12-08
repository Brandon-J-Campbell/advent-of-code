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

i = 0
result = 0
first = -1
second = -1
third = -1

for a in inputs:
    i = i + 1
    first = a
    for j in range(i, len(inputs) - 1):
        second = inputs[j]
        if (first + second) > 2020:
            continue
        
        for k in range(j, len(inputs) - 1):
            print(first + second + inputs[k])
            if first + second + inputs[k] == 2020:
                third = inputs[k]
                break
            
        if third > -1:
            break

    if third > -1:
        break

print(first * second * third)

f.close()

