from functools import reduce
from utils import *

inp = input_text()

primes = []


def parse_monkey(m: str):
    global primes

    _, sitems, op, test, ttrue, tfalse = m.strip().split("\n")
    _, sitems = sitems.split(":")

    _, op = op.split("=")
    op = op.strip()

    div = int(test.split("by")[1].strip())
    ttrue = int(ttrue.split("monkey")[1].strip())
    tfalse = int(tfalse.split("monkey")[1].strip())

    primes.append(div)

    return {
        "items": [int(n.strip()) for n in sitems.split(",")],
        "op": lambda old: eval(op),
        "div": div,
        "ttrue": ttrue,
        "tfalse": tfalse,
    }


ms = list(map(parse_monkey, inp.split("\n\n")))
N = reduce(op.mul, primes, 1)

ins = [0 for _ in ms]
for round in range(10000):
    print(round, ins)
    for i, m in enumerate(ms):
        for v in m["items"]:
            ins[i] += 1
            val = (m["op"](v)) % N
            target = m["ttrue"] if val % m["div"] == 0 else m["tfalse"]
            ms[target]["items"].append(val)
        m["items"].clear()

x, y = sorted(ins, reverse=True)[:2]
print(x * y)
