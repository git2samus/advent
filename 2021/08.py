#!/usr/bin/env python3
import fileinput
from pprint import pprint


digit_signals = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6,
}


def parse_input(input_stream):
    for line in input_stream:
        signal_patterns, digit_output = line.split("|")
        yield signal_patterns.split(), digit_output.split()


def solve(input_stream):
    len_digits = [v for k, v in digit_signals.items() if k in (1, 4, 7, 8)]

    count = 0
    for signal_patterns, digit_output in parse_input(input_stream):
        count += sum(1 for digits in digit_output if len(digits) in len_digits)

    return count


if __name__ == "__main__":
    answer = solve(fileinput.input())
    pprint(answer)
