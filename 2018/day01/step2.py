def get(dict, x):
    try:
        value = dict[x]
        print("Found " + str(value) + " at " + str(x))
        return True
    except:
        return False
    
def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
      
dict = { 0: 1}
result = 0
count = 0
found = False

while found == False:
    f = open("input.txt", "r") 
    for line in f:
        count += 1
        if RepresentsInt(line):
            result = result + int(line)
            if get(dict, result):
                print(result)
                found = True
            else:
                dict[result] = 1

    f.close()
print(count)
