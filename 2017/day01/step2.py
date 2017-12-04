def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
    
f = open("input.txt", "r")

input = f.read()

result = 0
halfLength = (len(input) - 1) / 2
for i in range(0, halfLength):
    c1 = input[i]
    c2 = input[halfLength + i]
   
    print(c1 + " - " + c2)
    if RepresentsInt(c1) and RepresentsInt(c2):
        if int(c1) == int(c2):
            result = result + (int(c1) * 2)
        
print(result)

f.close()
