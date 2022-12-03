f = open("input.txt", "r")

total = 0

for line in f:
    score = 0
    play = line.rstrip().split(" ")
    if play[0] == "A":
        if play[1] == "X":
            #Draw
            score = score + 4 # 1 for Rock, 3 for Draw
        elif play[1] == "Y":
            #Win
            score = score + 8 # 2 for Paper, 6 for Win
        elif play[1] == "Z":
            #Loss
            score = score + 3 # 3 for Scissors, 0 for Loss
    elif play[0] == "B":
        if play[1] == "X":
            #Loss
            score = score + 1 # 1 for Rock, 0 for Loss
        elif play[1] == "Y":
            #Draw
            score = score + 5 # 2 for Paper, 3 for Draw
        elif play[1] == "Z":
            #Win
            score = score + 9 # 3 for Scissors, 6 for Win
    else:
        if play[1] == "X":
            #Win
            score = score + 7 # 1 for Rock, 6 for Win
        elif play[1] == "Y":
            #Loss
            score = score + 2 # 2 for Paper, 0 for Loss
        elif play[1] == "Z":
            #Draw
            score = score + 6 # 3 for Scissors, 3 for Draw
    total = total + score
    
print(total)

f.close()
