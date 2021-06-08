#!/usr/bin/env python3
import fileinput

seen = set()
sums = dict()

for line in fileinput.input():
    v = int(line)

    if 2020 - v in sums:
        print(v * sums[2020 - v])
        break

    for vv in seen:
        sums[v + vv] = v * vv

    seen.add(v)
