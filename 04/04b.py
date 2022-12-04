from utils import *

total = 0
for l in input_lines():
    x, y = l.split(",")
    a, b = map(int, x.split("-"))
    c, d = map(int, y.split("-"))

    s1 = set(range(a, b + 1))
    s2 = set(range(c, d + 1))

    if len(s1 & s2) > 0:
        total += 1

print(total)
