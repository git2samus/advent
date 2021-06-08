#!/usr/bin/env python3
import re, fileinput

valid = 0

for line in fileinput.input():
    match = re.match('(?P<min>\d+)-(?P<max>\d+) (?P<char>\w): (?P<pwd>\w+)', line)
    min_c, max_c, char, pwd = int(match['min']), int(match['max']), match['char'], match['pwd']

    count = sum(1 for c in pwd if c == char)
    if min_c <= count <= max_c:
        valid += 1

print(valid)
