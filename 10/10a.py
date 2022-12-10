from utils import *

x = 1
cycle = 0

total = 0


def check():
    global total, cycle, x
    if cycle in {20, 60, 100, 140, 180, 220}:
        total += cycle * x


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

print(total)
