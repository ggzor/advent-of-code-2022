from utils import *
import math

# Change for each part
N = 10

positions = set()

values = [0 + 0j for _ in range(N)]

positions.add(values[-1])

# This is stupid, but works like a charm
deltas = {
    2 + 0j: 1 + 0j,
    -2 + 0j: -1 + 0j,
    0 + 2j: 0 + 1j,
    0 - 2j: 0 - 1j,
    1 + 2j: 1 + 1j,
    1 - 2j: 1 - 1j,
    2 + 1j: 1 + 1j,
    2 - 1j: 1 - 1j,
    -1 + 2j: -1 + 1j,
    -1 - 2j: -1 - 1j,
    -2 + 1j: -1 + 1j,
    -2 - 1j: -1 - 1j,
    1 + 0j: 0,
    -1 + 0j: 0,
    1 - 1j: 0,
    -1 - 1j: 0,
    -1 + 1j: 0,
    0 + 1j: 0,
    1 + 1j: 0,
    0 + 0j: 0,
    0 - 1j: 0,
    2 - 2j: 1 - 1j,
    -2 - 2j: -1 - 1j,
    -2 + 2j: -1 + 1j,
    2 + 2j: 1 + 1j,
}

for l in input_lines():
    d, n = l.split()
    for _ in range(int(n)):
        if d == "U":
            values[0] += 0 + -1j
        if d == "R":
            values[0] += 1 + 0j
        if d == "L":
            values[0] += -1 + 0j
        if d == "D":
            values[0] += 0 + 1j

        for i in range(1, len(values)):
            h = values[i - 1]
            t = values[i]
            t += deltas[h - t]
            values[i] = t

        positions.add(values[-1])

print(len(positions))
