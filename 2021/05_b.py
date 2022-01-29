#!/usr/bin/env python3
import fileinput
from collections import Counter
from pprint import pprint


def cmp(a, b):
    return (a > b) - (a < b)


def plot(start_coord, end_coord):
    delta_x = cmp(end_coord[0], start_coord[0])
    delta_y = cmp(end_coord[1], start_coord[1])

    current = start_coord
    while True:
        yield current

        if current == end_coord:
            break

        current = (current[0] + delta_x, current[1] + delta_y)


def parse_coord(raw):
    return tuple(map(int, raw.split(",")))


def parse_input(input_stream):
    for line in input_stream:
        start, _, end = line.split()

        start_coord = parse_coord(start)
        end_coord = parse_coord(end)

        for coord in plot(start_coord, end_coord):
            yield coord


def solve(input_stream):
    counts = Counter(parse_input(input_stream))

    return sum(1 for count in counts.values() if count > 1)


if __name__ == "__main__":
    answer = solve(fileinput.input())
    pprint(answer)
