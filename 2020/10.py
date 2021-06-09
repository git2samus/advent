#!/usr/bin/env python3
import fileinput
from collections import Counter

def iterpairs(iterable):
    prev, init = None, False

    for item in iterable:
        if init:
            yield prev, item
        else:
            init = True

        prev = item


seq = [0]
seq.extend(sorted(int(line) for line in fileinput.input()))
seq.append(seq[-1] + 3)

count = Counter(b - a for a, b in iterpairs(seq))
print(count[1] * count[3])
