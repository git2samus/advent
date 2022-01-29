#!/usr/bin/env python3
import fileinput
from pprint import pprint


def parse_input(input_stream):
    for line in input_stream:
        return tuple(map(int, line.strip().split(",")))


def solve(input_stream, iterations):
    state = parse_input(input_stream)

    new_state = []
    for _ in range(iterations):
        for fish in state:
            if fish == 0:
                new_state.extend((6, 8))
            else:
                new_state.append(fish - 1)

        state = new_state
        new_state = []

    return len(state)


if __name__ == "__main__":
    answer = solve(fileinput.input(), 80)
    pprint(answer)
