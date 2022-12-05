from utils import *

p1, p2 = input_text().split("\n\n")
ls = p1.split("\n")
stacks = list(
    list(x for x in reversed(l) if x != " ")[1:] for l in zip(*ls) if l[-1].isnumeric()
)

for l in p2.strip().split("\n"):
    c, f, t = list_int(re.findall(r"\b\d+\b", l))

    for _ in range(c):
        stacks[t - 1].append(stacks[f - 1].pop())

print("".join(s[-1] for s in stacks))
