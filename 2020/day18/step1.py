def evaluate(equation, start):
    first = None
    operator = ""

    i = start

    while i < len(equation):
        if equation[i] == ")":
            return [first, i + 1]

        if equation[i] == " ":
            i = i + 1
            continue

        if equation[i] == "(":
            result = evaluate(equation, i + 1)
            if operator == "+":
                first = first + result[0]
            elif operator == "*":
                first = first * result[0]
            else:
                first = result[0]
            operator = ""
            i = result[1]
        elif equation[i] == "+":
            operator = "+"
            i = i + 1
        elif equation[i] == "*":
            operator = "*"
            i = i + 1
        else:
            remainingEquation = equation[i:len(equation)]
            nextSpace = -1
            if remainingEquation.find(")") >= 0 and remainingEquation.find(" ") >= 0:
                nextSpace = min(remainingEquation.find(" "), remainingEquation.find(")"))
            elif remainingEquation.find(" ") >= 0:
                nextSpace = remainingEquation.find(" ")
            elif remainingEquation.find(")") >= 0:
                nextSpace = remainingEquation.find(")")
                
            if nextSpace == -1:
                nextSpace = len(remainingEquation)
            i = i + nextSpace
            if (first == None):
                first = int(remainingEquation[0:nextSpace])
            else:
                second = int(remainingEquation[0:nextSpace])
                if operator == "+":
                    first = first + second
                elif operator == "*":
                    first = first * second
                operator = ""
    return [first, i + 1]
    
f = open("input.txt", "r")

result = 0
for line in f:
    line = line.rstrip()
    result = result + evaluate(line, 0)[0]
        
print(result)
f.close()
