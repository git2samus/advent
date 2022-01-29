#!/usr/bin/env python3
import fileinput
from pprint import pprint


def parse_input(input_stream):
    for line in input_stream:
        return tuple(map(int, line.strip().split(",")))


def solve(input_stream):
    positions = parse_input(input_stream)

    fuel = None
    for n in range(min(positions), max(positions) + 1):
        n_sum = sum(abs(pos - n) for pos in positions)

        if fuel is None or n_sum < fuel:
            fuel = n_sum

    return fuel


if __name__ == "__main__":
    answer = solve(fileinput.input())
    pprint(answer)
