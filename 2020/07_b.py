#!/usr/bin/env python3
import fileinput


rules = {}

for line in fileinput.input():
    bag, contents = line.split(' bags contain ')

    counts = {}
    if not contents.startswith('no'):
        for content in contents.split(', '):
            parts = content.split()
            factor, content_bag = int(parts[0]), ' '.join(parts[1:3])

            counts[content_bag] = factor

    rules[bag] = counts


def track_target(target):
    return sum(factor * (1 + track_target(content_bag)) for content_bag, factor in rules[target].items())

target = 'shiny gold'
print(track_target(target))
