from utils import *

x = 1
cycle = 0
row = 0
total = 0

W = 40
H = 6
CRT = [["."] * W for _ in range(H)]


def check():
    global total, cycle, x
    col = (cycle - 1) % W
    row = (cycle - 1) // W

    if x - 1 <= col <= x + 1:
        CRT[row][col] = "#"


for l in input_lines():
    inst = l.split()
    if inst[0] == "noop":
        cycle += 1
        check()
    else:
        _, amount = inst
        cycle += 1
        check()
        cycle += 1
        check()
        x += int(amount)

print("\n".join("".join(l) for l in CRT))
