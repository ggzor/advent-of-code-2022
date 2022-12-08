from functools import reduce
from utils import *

g = [list(map(int, l)) for l in input_text().strip().splitlines()]

h = len(g)
w = len(g[0])

best = int(-1e9)
for r in range(1, h - 1):
    for c in range(1, w - 1):
        x = g[r][c]
        vs = [0]

        ri, ci = r, c - 1
        while ci >= 0:
            if g[ri][ci] >= x:
                vs[-1] += 1
                break
            else:
                vs[-1] += 1
            ci -= 1

        vs.append(0)
        ri, ci = r, c + 1
        while ci < w:
            if g[ri][ci] >= x:
                vs[-1] += 1
                break
            else:
                vs[-1] += 1
            ci += 1

        vs.append(0)
        ri, ci = r - 1, c
        while ri >= 0:
            if g[ri][ci] >= x:
                vs[-1] += 1
                break
            else:
                vs[-1] += 1
            ri -= 1

        vs.append(0)
        ri, ci = r + 1, c
        while ri < h:
            if g[ri][ci] >= x:
                vs[-1] += 1
                break
            else:
                vs[-1] += 1
            ri += 1

        best = max(best, reduce(op.mul, vs))

print(best)
