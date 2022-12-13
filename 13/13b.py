from utils import *


def right_order(l1, l2):
    if isinstance(l1, int) and isinstance(l2, int):
        if l1 < l2:
            return -1
        elif l1 == l2:
            return 0
        else:
            return 1
    elif isinstance(l1, list) and isinstance(l2, list):
        for v1, v2 in it.zip_longest(l1, l2, fillvalue=None):
            if v1 == None:
                return -1
            if v2 == None:
                return 1
            cval = right_order(v1, v2)
            if cval == 0:
                continue
            else:
                return cval
        return 0
    else:
        if isinstance(l1, int):
            return right_order([l1], l2)
        else:
            return right_order(l1, [l2])


values = [[[2]], [[6]]]

total = 0
for i, block in enumerate(input_text().split("\n\n")):
    l1, l2 = map(eval, block.strip().split("\n"))
    values.append(l1)
    values.append(l2)

values = sorted(values, key=functools.cmp_to_key(right_order))

print((1 + values.index([[2]])) * (1 + values.index([[6]])))
