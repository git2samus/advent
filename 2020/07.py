#!/usr/bin/env python3
import fileinput
from collections import defaultdict


rules = defaultdict(set)

for line in fileinput.input():
    bag, contents = line.split(' bags contain ')

    if contents.startswith('no'):
        contents = {None}
    else:
        contents = {' '.join(content.split()[1:3]) for content in contents.split(', ')}

    for content in contents:
        rules[content].add(bag)


def track_target(target, seen=None):
    if seen is None:
        seen = set()

    for match in rules[target]:
        if match not in seen:
            seen.add(match)
            track_target(match, seen)

    return seen

target = 'shiny gold'
print(len(track_target(target)))
