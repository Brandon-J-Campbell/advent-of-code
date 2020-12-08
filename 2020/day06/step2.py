def countChar(c, s):
    count = 0
    for i in range(len(s)):
        if (s[i] == c):
            count = count + 1
    return count

def validAnswers(answers):
    answerDict = {}
    validAnswers = 0
    
    for answer in answers:
        for i in range(len(answer)):
            if answer[i] not in answerDict:
                answerDict[answer[i]] = 1
            else:
                answerDict[answer[i]] = answerDict[answer[i]] + 1
    
    print(answerDict)
    for value in answerDict.values():
        if value == len(answers):
            validAnswers = validAnswers + 1
            
    return validAnswers
    
f = open("input.txt", "r")

result = 0
answers = []

for line in f:
    if line == "\n":
        result = result + validAnswers(answers)
        answers = []
        continue
        
    answers.append(line.rstrip())

result = result + validAnswers(answers)
print(result)

f.close()
