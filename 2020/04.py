#!/usr/bin/env python3
import fileinput

def parse(raw):
    items = raw.split()
    res = {}

    for item in items:
        k, v = item.split(':')
        res[k] = v

    return res


passports = []

current = ''
for line in fileinput.input():
    line = line.strip()

    if line:
        current += ' ' + line
    else:
        passports.append(parse(current))
        current = ''

passports.append(parse(current))

req_fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
print(sum(1 for p in passports if all(k in p for k in req_fields)))
