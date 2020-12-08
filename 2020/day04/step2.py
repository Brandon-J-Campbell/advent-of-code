def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
        
def countChar(c, s):
    count = 0
    for i in range(len(s)):
        if (s[i] == c):
            count = count + 1
    return count

def ecl(s):
    validColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if s in validColors:
        return True
    return False
    
def pid(s):
    if len(s) == 9 and RepresentsInt(s):
        return True
    return False
    
def eyr(s):
    if RepresentsInt(s):
        if int(s) >= 2020 and int(s) <= 2030:
            return True
    return False
    
def byr(s):
    if RepresentsInt(s):
        if int(s) >= 1920 and int(s) <= 2002:
            return True
    return False
    
def iyr(s):
    if RepresentsInt(s):
        if int(s) >= 2010 and int(s) <= 2020:
            return True
    return False
    
def hgt(s):
    measurement = s[-2:]
    height = s.rstrip(s[-2:])
    if measurement == "in":
        if RepresentsInt(height):
            if int(height) >= 59 and int(height) <= 76:
                return True
    elif measurement == "cm":
        if RepresentsInt(height):
            if int(height) >= 150 and int(height) <= 193:
                return True
    return False
    
def hcl(s):
    if len(s) == 7:
        for i in range(len(s)):
            if i == 0:
                if s[i] != "#":
                    return False
            else:
                validChars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
                if s[i] not in validChars:
                    return False
        return True
    return False
            
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
        else:
            if field == "ecl":
                if not ecl(passport[field]):
                    print("ecl not valid: " + passport[field])
                    valid = 0
                    break
            elif field == "pid":
                if not pid(passport[field]):
                    print("pid not valid: " + passport[field])
                    valid = 0
                    break
            elif field == "eyr":
                if not eyr(passport[field]):
                    print("eyr not valid: " + passport[field])
                    valid = 0
                    break
            elif field == "byr":
                if not byr(passport[field]):
                    print("byr not valid: " + passport[field])
                    valid = 0
                    break
            elif field == "iyr":
                if not iyr(passport[field]):
                    print("iyr not valid: " + passport[field])
                    valid = 0
                    break
            elif field == "hgt":
                if not hgt(passport[field]):
                    print("hgt not valid: " + passport[field])
                    valid = 0
                    break
            elif field == "hcl":
                if not hcl(passport[field]):
                    print("hcl not valid: " + passport[field])
                    valid = 0
                    break
            
    result = result + valid
        
print(result)

f.close()
