#!/usr/bin/env python3
import sys, fileinput
from collections import deque


target = int(sys.argv[1])
terms = deque()

for line in fileinput.input(sys.argv[2:]):
    num = int(line)

    terms.append(num)
    while sum(terms) > target:
        terms.popleft()

    if sum(terms) == target:
        print(min(terms) + max(terms))
        break
