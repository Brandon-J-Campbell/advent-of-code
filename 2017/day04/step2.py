def get(dict, c):
    try:
        value = dict[c]
        return True
    except:
        return False

def compare(master, dict):
    if len(master.items()) != len(dict.items()):
        print("Length not the same!")
        return False

    for k, v in master.items():
        if not get(dict, k):
            print(k + " does not exist in dict!")
            return False

        if master[k] != dict[k]:
            print(str(master[k]) + " does not equal " + str(dict[k]) + "!")
            return False
    
    return True

f = open("input.txt", "r")

result = 0

for line in f:
    duplicates = 0
    array = line.rstrip().split(" ")
    for i in range(0, len(array)):
        if duplicates == 0:
            masterDict = {}
            for c in array[i]:
                if get(masterDict, c):
                    masterDict[c] = masterDict[c] + 1
                else:
                    masterDict[c] = 1
            for j in range(i + 1, len(array)):
                if duplicates == 0:
                    print("Comparing " + array[i] + " and " + array[j])
                    dict = {}
                    for ch in array[j]:
                        if get(dict, ch):
                            dict[ch] = dict[ch] + 1
                        else:
                            dict[ch] = 1

                    print(masterDict)
                    print(dict)             
                    if compare(masterDict, dict):
                        print("Found duplicate!")
                        duplicates = duplicates + 1

    if duplicates == 0:
        print("No duplicate found on " + line)
        result = result + 1

print(result)

f.close()
