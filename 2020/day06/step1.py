def countChar(c, s):
    count = 0
    for i in range(len(s)):
        if (s[i] == c):
            count = count + 1
    return count

def uniqueAnswers(answers):
    answerDict = {}
    for answer in answers:
        for i in range(len(answer)):
            answerDict[answer[i]] = 1
    
    print(answerDict)
    return len(answerDict)
    
f = open("input.txt", "r")

result = 0
answers = []

for line in f:
    if line == "\n":
        result = result + uniqueAnswers(answers)
        answers = []
        continue
        
    answers.append(line.rstrip())

result = result + uniqueAnswers(answers)
print(result)

f.close()
