def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
        
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
        
result = 0

for ticket in nearbyTickets:
    for value in ticket:
        valid = False
        for key in rules.keys():
            if value in rules[key]:
                valid = True
                break
                
        if not valid:
            result = result + value

print(result)
f.close()
