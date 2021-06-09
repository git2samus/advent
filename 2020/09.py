#!/usr/bin/env python3
import sys, fileinput

preamble_size = int(sys.argv[1])
preamble = []

for line in fileinput.input(sys.argv[2:]):
    num = int(line)

    if len(preamble) == preamble_size:
        valid = False

        for i, n in enumerate(preamble[:-1]):
            if num - n in preamble[i+1:]:
                valid = True
                break

        if not valid:
            print(num)
            break

    preamble.append(num)
    preamble = preamble[-preamble_size:]
