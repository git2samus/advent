#!/usr/bin/env python3
import math
import fileinput
from functools import cache
from pprint import pprint


@cache
def sum_children(fish_timer, iterations):
    child_count = math.ceil(max(0, iterations - fish_timer) / 7)

    for skips in range(child_count):
        child_count += sum_children(8, iterations - fish_timer - 7 * skips - 1)

    return child_count


def parse_input(input_stream):
    for line in input_stream:
        return tuple(map(int, line.strip().split(",")))


def solve(input_stream, iterations):
    state = parse_input(input_stream)

    fish_count = len(state)
    for fish_timer in state:
        fish_count += sum_children(fish_timer, iterations)

    return fish_count


if __name__ == "__main__":
    #answer = solve(fileinput.input(), 18)
    #answer = solve(fileinput.input(), 80)
    answer = solve(fileinput.input(), 256)
    pprint(answer)
