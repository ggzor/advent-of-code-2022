from utils import *

fs = {}
pwd = []
lines = mit.peekable(iter(input_lines()))


def add_path(k, v):
    target = fs
    for part in pwd:
        if not part in target:
            target[part] = {}
        target = target[part]
    target[k] = v


try:
    while True:
        l = next(lines)
        if l.startswith("$ cd"):
            if l == "$ cd /":
                pwd = []
            elif l == "$ cd ..":
                pwd = pwd[:-1]
            else:
                dir = l.split(" ")[2]
                pwd.append(dir)
        elif l.startswith("$ ls"):
            while not lines.peek("$").startswith("$"):
                l = next(lines)
                if l.startswith("dir"):
                    name = l.split(" ")[1]
                    add_path(name, {})
                else:
                    size, name = l.split(" ")
                    add_path(name, int(size))
except StopIteration:
    pass

TOTAL = 70000000
UNUSED_DESIRED = 30000000


sizes = {}


def traverse(path, target):
    size = 0
    for k, v in target.items():
        if isinstance(v, dict):
            size += traverse((*path, k), v)
        else:
            size += v
    sizes[path] = size
    return size


traverse(tuple([]), fs)

used = sizes[tuple([])]
to_release = UNUSED_DESIRED - (TOTAL - used)

for s in sorted(sizes.values()):
    if s >= to_release:
        print(s)
        break
