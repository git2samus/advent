#!/usr/bin/env python3
import fileinput

groups = []
current = None

for line in fileinput.input():
    line = line.strip()

    if line:
        if current is None:
            current = set(line)
        else:
            current.intersection_update(line)
    else:
        groups.append(current)
        current = None

groups.append(current)

print(sum(len(g) for g in groups))
