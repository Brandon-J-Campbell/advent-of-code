def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
    
f = open("input.txt", "r")

result = 0

for line in f:
    value = 0
    array = line.split("\t")
    for i in range(0, len(array)):
        print("i = " + str(i))
        if value == 0 and len(array) > 1:
            for j in range(i, len(array)):
                print("Comparing " + array[i] + " and " + array[j])
                if RepresentsInt(array[i]) and RepresentsInt(array[j]) and value == 0:
                    left = int(array[i])
                    right = int(array[j])
                    if left < right:
                        if right % left == 0:
                            value = right / left
                            print("Found value with " + array[i] + " and " + array[j] + ": " + str(value))
                    elif right < left:    
                        if left % right == 0:
                            value = left / right
                            print("Found value with " + array[i] + " and " + array[j] + ": " + str(value))
                  
    result = result + value
    print(result)
    print("\n")

print(result)

f.close()
