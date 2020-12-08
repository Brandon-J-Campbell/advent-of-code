def countChar(c, s):
    count = 0
    for i in range(len(s)):
        if (s[i] == c):
            count = count + 1
    return count

f = open("input.txt", "r")

result = 0
reqFields = ["ecl", "pid", "eyr", "byr", "iyr", "hgt", "hcl"]
passports = []
buffer = {}

for line in f:
    if line == "\n":
        passports.append(buffer)
        buffer = {}
        continue
        
    lineArray = line.rstrip().split(" ")
    for item in lineArray:
        itemArray = item.rstrip().split(":")
        buffer[itemArray[0]] = itemArray[1]
passports.append(buffer)

print(len(passports))
for passport in passports:
    valid = 1
    for field in reqFields:
        if field not in passport:
            valid = 0
            break
            
    result = result + valid
        
print(result)

f.close()
