#!/usr/bin/env python3
import fileinput
from itertools import pairwise
from collections import Counter
from pprint import pprint


def parse_input(input_stream):
    polymer, rules = None, {}

    for line in input_stream:
        line = line.strip()
        if not line:
            continue

        if polymer is None:
            polymer = line
        else:
            pair, _, insertion = line.split()
            rules[tuple(pair)] = insertion

    return polymer, rules


def evolve_polymer(polymer, rules, iterations):
    for iteration in range(iterations):
        new_polymer = [polymer[0]]

        for pair in pairwise(polymer):
            if pair in rules:
                new_polymer.append(rules[pair])

            new_polymer.append(pair[1])

        polymer = "".join(new_polymer)

    return polymer


def solve(input_stream, iterations):
    inital_polymer, rules = parse_input(input_stream)

    final_polymer = evolve_polymer(inital_polymer, rules, iterations)
    count = Counter(final_polymer)

    most_common = count.most_common()
    return most_common[0][1] - most_common[-1][1]


if __name__ == "__main__":
    answer = solve(fileinput.input(), 40)
    pprint(answer)
