def evaluate(equation):
    first = None
    operator = ""

    paren = equation.find("(")
    endparen = -1
    while paren > -1:
        parenCount = 1
        for i in range(paren + 1, len(equation)):
            if equation[i] == "(":
                parenCount = parenCount + 1
            elif equation[i] == ")":
                parenCount = parenCount - 1
                
            if parenCount == 0:
                endparen = i
                break
        
        result = evaluate(" " + equation[paren + 1:endparen] + " ")
        equation = equation.replace(equation[paren:endparen + 1], str(result))
        paren = equation.find("(")
    
    print("New equation: " + equation)
    i = 0
    
    while True:
        if i == len(equation):
            break
            
        if equation[i] == " ":
            i = i + 1
            continue

        if equation[i] == "+":
            operator = "+"
            i = i + 1
        elif equation[i] == "*":
            operator = "*"
            i = i + 1
        else:
            remainingEquation = equation[i:len(equation)]
            nextSpace = -1
            if remainingEquation.find(" ") >= 0:
                nextSpace = remainingEquation.find(" ")
                
            if nextSpace == -1:
                nextSpace = len(remainingEquation)
            i = i + nextSpace
            if (first == None):
                first = int(remainingEquation[0:nextSpace])
            else:
                second = int(remainingEquation[0:nextSpace])
                if operator == "+":
                    result = first + second
                    stringToReplace = " " + str(first) + " + " + str(second) + " "
                    print(equation)
                    print(stringToReplace)
                    equation = equation.replace(stringToReplace, " " + str(result) + " ")
                    first = None
                    i = 0
                elif operator == "*":
                    if equation.find("+") > -1:
                        first = second
                    else:
                        result = first * second
                        stringToReplace = " " + str(first) + " * " + str(second) + " "
                        equation = equation.replace(stringToReplace, " " + str(result) + " ")
                        first = None
                        i = 0
                operator = ""
    
    return int(equation)
    
f = open("input.txt", "r")

result = 0
for line in f:
    line = " " + line.rstrip() + " "
    print(line + " = " + str(evaluate(line)))
    result = result + evaluate(line)
        
print(result)
f.close()
