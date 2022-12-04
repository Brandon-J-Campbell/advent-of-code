f = open("input.txt", "r")

total = 0

for line in f:
    inputs = line.rstrip().split(",")
    elf1 = inputs[0].split("-")
    elf2 = inputs[1].split("-")
    if int(elf1[0]) >= int(elf2[0]) and int(elf1[0]) <= int(elf2[1]):
        total = total + 1
        continue

    if int(elf1[1]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1]):
        total = total + 1
        continue

    if int(elf2[0]) >= int(elf1[0]) and int(elf2[0]) <= int(elf1[1]):
        total = total + 1
        continue

    if int(elf2[1]) >= int(elf1[0]) and int(elf2[1]) <= int(elf1[1]):
        total = total + 1
        continue

print(total)

f.close()

