from sys import argv
import math

result = 0
input = int(argv[1])

odd = int(math.sqrt(input - 1))
if odd % 2 == 0:
    odd = odd - 1
box = (odd + 1) / 2

start = (odd ** 2) + box
d = 0

if input < start:
    d = start - input
else:
    old = start
    while start < input:
        old = start
        start = start + (box * 2)
    d = min(start - input, input - old)

result = box + d

print(result)

