#!/usr/bin/env python3
import fileinput

trees, pos = 0, 0

for line in fileinput.input():
    line = line.strip()

    if line[pos] == '#':
        trees += 1

    pos = (pos + 3) % len(line)

print(trees)
