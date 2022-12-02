import re
            
            
    
f = open("input.txt", "r")

result = 0
rules = {}
messages = []
seenNewline = False
for line in f:
    print(line)
    if line == "\n":
        seenNewline = True
        continue
        
    line = line.rstrip()
    
    if not seenNewline:
        lineArray = line.split(":")
        ruleArray = lineArray[1].lstrip().split("|")
        rulesArray = []
        for rule in ruleArray:
            rulesArray.append(rule.lstrip().rstrip().split(" "))
        rules[lineArray[0]] = rulesArray
    else:
        messages.append(line)
        
print(rules)
print(messages)
        
print(result)
f.close()
