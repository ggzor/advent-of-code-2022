from utils import *

adj = defaultdict(list)

grid = [[c for c in l] for l in input_lines()]
W = len(grid[0])
H = len(grid)


for row in range(H):
    for col in range(W):
        x = grid[row][col]
        if x == "S":
            start = (row, col)
            xvalue = ord("a")
        elif x == "E":
            end = (row, col)
            xvalue = ord("z")
        else:
            xvalue = ord(x)

        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if not (dr == 0 and dc == 0) and (dr == 0 or dc == 0):
                    tr = row + dr
                    tc = col + dc

                    if 0 <= tr < H and 0 <= tc < W:
                        y = grid[tr][tc]

                        if y == "S":
                            yvalue = ord("a")
                        elif y == "E":
                            yvalue = ord("z")
                        else:
                            yvalue = ord(y)

                        if xvalue + 1 >= yvalue:
                            adj[(row, col)].append((tr, tc))


def dist(p1, p2):
    y1, x1 = p1
    y2, x2 = p2
    return abs(y1 - y2) + abs(x1 - x2)


def f(p, depth):
    return depth + dist(p, end)


n = 0
gs = defaultdict(lambda: float("inf"))
fs = defaultdict(lambda: float("inf"))

gs[start] = 0
fs[start] = dist(start, end)

open_nodes = [(fs[start], 0, start)]

while open_nodes:
    n += 1

    _, gv, cur = heappop(open_nodes)
    if gv < gs[cur]:
        continue

    if cur == end:
        break

    for neigh in adj[cur]:
        next_gs = gs[cur] + 1
        if next_gs < gs[neigh]:
            gs[neigh] = next_gs
            fs[neigh] = next_gs + dist(neigh, end)
            heappush(open_nodes, (fs[neigh], n, neigh))

print(gs[end])
