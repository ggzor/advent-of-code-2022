import sys
from collections import defaultdict

maxr = -1e9

gr = defaultdict(lambda: True)
for l in sys.stdin:
    ps = l.strip().split("->")
    for b1, b2 in zip(ps, ps[1:]):
        c1, r1, c2, r2 = map(int, b1.split(",")+b2.split(","))
        maxr = max(maxr, r1, r2)
        if r1 == r2:
            if c1 > c2:
                c1, c2 = c2, c1
            for cv in range(c1, c2 + 1):
                gr[r1, cv] = False
        if c1 == c2:
            if r1 > r2:
                r1, r2 = r2, r1
            for rv in range(r1, r2 + 1):
                gr[rv, c1] = False

fr = maxr + 2

sand = 0
try:
    while True:
        sr, sc = 0, 500
        if not gr[sr, sc]:
            break
        while True:
            if sr + 1 == fr:
                break
            elif gr[sr + 1, sc]:
                sr += 1
            elif gr[sr + 1, sc - 1]:
                sr += 1
                sc -= 1
            elif gr[sr + 1, sc + 1]:
                sr += 1
                sc += 1
            else:
                break
        sand += 1
        gr[sr, sc] = False
except AssertionError:
    pass

print(sand)
