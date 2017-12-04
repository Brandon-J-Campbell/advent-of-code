f = open("input.txt", "r")

result = 0

for line in f:
    duplicates = 0
    array = line.rstrip().split(" ")
    for i in range(0, len(array)):
        if duplicates == 0 and len(array) > 1:
            for j in range(i + 1, len(array)):
                print("Comparing " + array[i] + " and " + array[j])
                if array[i] == array[j]:
                    print("Found duplicate!")
                    duplicates = duplicates + 1
    if duplicates == 0:
        print("No duplicate found on " + line)
        result = result + 1

print(result)

f.close()
