#!/usr/bin/env python3
import fileinput

seen = set()

for line in fileinput.input():
    v = int(line)

    if 2020 - v in seen:
        print(v * (2020 - v))
        break

    seen.add(v)
