from utils import *

s = 0

for l in input_lines():
    p1 = set(l[: len(l) // 2])
    p2 = set(l[len(l) // 2 :])

    ps = p1 & p2
    for p in ps:
        if p.isupper():
            s += 27 + (ord(p) - ord("A"))
        else:
            s += 1 + (ord(p) - ord("a"))

print(s)
