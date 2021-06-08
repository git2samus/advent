#!/usr/bin/env python3
import re, fileinput

valid = 0

for line in fileinput.input():
    match = re.match('(?P<min>\d+)-(?P<max>\d+) (?P<char>\w): (?P<pwd>\w+)', line)
    min_c, max_c, char, pwd = int(match['min']), int(match['max']), match['char'], match['pwd']

    count = sum(char == pwd[p-1] for p in (min_c, max_c))
    if count == 1:
        valid += 1

print(valid)
