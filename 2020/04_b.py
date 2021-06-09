#!/usr/bin/env python3
import re, fileinput

def parse(raw):
    items = raw.split()
    res = {}

    for item in items:
        k, v = item.split(':')
        res[k] = v

    return res

def valid(k, v):
    if k == 'byr':
        return re.match('\d+$', v) and 1920 <= int(v) <= 2002

    if k == 'iyr':
        return re.match('\d+$', v) and 2010 <= int(v) <= 2020

    if k == 'eyr':
        return re.match('\d+$', v) and 2020 <= int(v) <= 2030

    if k == 'hgt':
        match = re.match('(\d+)(cm|in)$', v)
        if match:
            v, u = match.groups()
            if u == 'cm':
                return 150 <= int(v) <= 193
            if u == 'in':
                return 59 <= int(v) <= 76

    if k == 'hcl':
        return re.match('#[0-9a-f]{6}$', v)

    if k == 'ecl':
        return re.match('(amb|blu|brn|gry|grn|hzl|oth)$', v)

    if k == 'pid':
        return re.match('\d{9}$', v)


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
print(sum(1 for p in passports if all(k in p and valid(k, p[k]) for k in req_fields)))
