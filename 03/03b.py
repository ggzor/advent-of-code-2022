from utils import *

s = 0

for l1, l2, l3 in mit.chunked(input_lines(), 3):
    ps = set(l1) & set(l2) & set(l3)
    for p in ps:
        if p.isupper():
            s += 27 + (ord(p) - ord("A"))
        else:
            s += 1 + (ord(p) - ord("a"))

print(s)
