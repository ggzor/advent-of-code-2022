from utils import *

elfs = []

for g in input_text().strip().split("\n\n"):
    ds = list_int(g.split("\n"))
    elfs.append(sum(ds))

print(sum(sorted(elfs, reverse=True)[:3]))
