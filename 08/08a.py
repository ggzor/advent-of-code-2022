from functools import reduce
from utils import *

g = [list(map(int, l)) for l in input_text().strip().splitlines()]

h = len(g)
w = len(g[0])

visible = set()

for r in range(h):
    best = int(-1e9)
    for c in range(w):
        x = g[r][c]
        if x > best:
            visible.add((r, c))
        best = max(best, x)

for r in range(h):
    best = int(-1e9)
    for c in range(w - 1, -1, -1):
        x = g[r][c]
        if x > best:
            visible.add((r, c))
        best = max(best, x)

for c in range(w):
    best = int(-1e9)
    for r in range(h):
        x = g[r][c]
        if x > best:
            visible.add((r, c))
        best = max(best, x)

for c in range(w - 1, -1, -1):
    best = int(-1e9)
    for r in range(h - 1, -1, -1):
        x = g[r][c]
        if x > best:
            visible.add((r, c))
        best = max(best, x)

print(len(visible))
