#!/usr/bin/env python3
import fileinput
from collections import Counter
from pprint import pprint


def plot(start_coord, end_coord):
    if start_coord[0] == end_coord[0]:
        return tuple(
            (start_coord[0], y)
            for y in range(
                min(start_coord[1], end_coord[1]),
                max(start_coord[1], end_coord[1]) + 1
            )
        )
    elif start_coord[1] == end_coord[1]:
        return tuple(
            (x, start_coord[1])
            for x in range(
                min(start_coord[0], end_coord[0]),
                max(start_coord[0], end_coord[0]) + 1
            )
        )

    return tuple()


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
