#!/usr/bin/env python3
import fileinput

groups = []
current = set()

for line in fileinput.input():
    line = line.strip()

    if line:
        current.update(line)
    else:
        groups.append(current)
        current = set()

groups.append(current)

print(sum(len(g) for g in groups))
