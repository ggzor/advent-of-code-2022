from utils import *

inp = input_text()


def parse_monkey(m: str):
    _, sitems, op, test, ttrue, tfalse = m.strip().split("\n")
    _, sitems = sitems.split(":")

    _, op = op.split("=")
    op = op.strip()

    div = int(test.split("by")[1].strip())
    ttrue = int(ttrue.split("monkey")[1].strip())
    tfalse = int(tfalse.split("monkey")[1].strip())

    return {
        "items": Counter(int(n.strip()) for n in sitems.split(",")),
        "op": lambda old: eval(op),
        "div": div,
        "ttrue": ttrue,
        "tfalse": tfalse,
    }


ms = list(map(parse_monkey, inp.split("\n\n")))

ins = [0 for _ in ms]
prev = [0 for _ in ms]
for round in range(20):
    for i, m in enumerate(ms):
        for k, v in m["items"].items():
            ins[i] += v
            val = m["op"](k) // 3
            target = m["ttrue"] if val % m["div"] == 0 else m["tfalse"]
            ms[target]["items"][val] += v
        m["items"].clear()

x, y = sorted(ins, reverse=True)[:2]
print(x * y)
