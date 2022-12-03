f = open("input.txt", "r")

total = 0

for line in f:
    score = 0
    play = line.rstrip().split(" ")
    if play[0] == "A":
        if play[1] == "X": #Rock
            #Scissors/Lose
            score = score + 3 # 3 for Scissors, 0 for Loss
        elif play[1] == "Y":
            #Rock/Draw
            score = score + 4 # 1 for Rock, 3 for Draw
        elif play[1] == "Z":
            #Paper/Win
            score = score + 8 # 2 for Paper, 6 for Win
    elif play[0] == "B": #Paper
        if play[1] == "X":
            #Rock/Lose
            score = score + 1 # 1 for Rock, 0 for Loss
        elif play[1] == "Y":
            #Paper/Draw
            score = score + 5 # 2 for Paper, 3 for Draw
        elif play[1] == "Z":
            #Scissors/Win
            score = score + 9 # 3 for Scissors, 6 for Win
    else: #Scissors
        if play[1] == "X":
            #Paper/Lose
            score = score + 2 # 2 for Paper, 0 for Loss    
        elif play[1] == "Y":
            #Scissors/Draw
            score = score + 6 # 3 for Scissors, 3 for Draw
        elif play[1] == "Z":
            #Rock/Win
            score = score + 7 # 1 for Rock, 6 for Win

    total = total + score
    
print(total)

f.close()

