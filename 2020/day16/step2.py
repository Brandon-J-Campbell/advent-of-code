f = open("input.txt", "r")

rules = {}
myTicket = []
nearbyTickets = []

step = 0
for line in f:
    line = line.rstrip()
    if len(line) == 0:
        step = step + 1
        continue
        
    if step == 0:
        lineArray = line.split(":")
        rulesArray = lineArray[1].split(" or ")
        validNumbers = []
        for rule in rulesArray:
            numArray = rule.split("-")
            for i in range(int(numArray[0]), int(numArray[1]) + 1):
                validNumbers.append(i)
        rules[lineArray[0]] = validNumbers
    elif step == 1:
        if line == "your ticket:":
            continue
        
        myTicketValues = line.split(",")
        for value in myTicketValues:
            myTicket.append(int(value))
    else:
        if line == "nearby tickets:":
            continue
        
        ticketValues = line.split(",")
        ticket = []
        for value in ticketValues:
            ticket.append(int(value))
        nearbyTickets.append(ticket)
        
validTickets = []
for ticket in nearbyTickets:
    ticketValid = True
    for value in ticket:
        valid = False
        for key in rules.keys():
            if value in rules[key]:
                valid = True
                break
                
        if not valid:
            ticketValid = False
    if ticketValid:
        validTickets.append(ticket)

ruleCount = len(validTickets[0])
rulesPosition = {}
for key in rules.keys():
    validSpots = []
    for i in range(ruleCount):
        validSpots.append(i)
    rulesPosition[key] = validSpots
    
for ticket in validTickets:
    for i in range(len(ticket)):
        value = ticket[i]
        for key in rules.keys():
            if value not in rules[key]:
                if i in rulesPosition[key]:
                    rulesPosition[key].remove(i)
    
    changes = True
    while changes:
        changes = False
        for key in rulesPosition.keys():
            if len(rulesPosition[key]) == 1:
                i = rulesPosition[key][0]
                for newkey in rulesPosition.keys():
                    if newkey != key and i in rulesPosition[newkey]:
                        changes = True
                        rulesPosition[newkey].remove(i)
    
    exit = True
    for key in rulesPosition.keys():
        if len(rulesPosition[key]) > 1:
            exit = False
            break
    
    if exit:
        break
        
result = 1
for key in rulesPosition.keys():
    if "departure" in key:
        result = result * myTicket[rulesPosition[key][0]]
        
print(result)
f.close()
