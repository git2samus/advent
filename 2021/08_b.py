#!/usr/bin/env python3
import fileinput
from collections import defaultdict
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


def decipher(signal_patterns):
    lengths = defaultdict(list)
    for pattern in signal_patterns:
        lengths[len(pattern)].append(pattern)

    mapping = [None] * 7

    mapping[0] = (set(lengths[3][0]) - set(lengths[2][0])).pop()

    known = set(lengths[2][0]) | set(lengths[3][0]) | set(lengths[4][0])
    for len_6 in lengths[6]:
        extra = set(len_6) - known
        if len(extra) == 1:
            mapping[6] = extra.pop()
            break

    known.add(mapping[6])
    for len_5 in lengths[5]:
        extra = set(len_5) - known
        if len(extra) == 1:
            mapping[4] = extra.pop()
            break

    known = set(lengths[3][0]) | set([mapping[4], mapping[6]])
    for len_6 in lengths[6]:
        extra = set(len_6) - known
        if len(extra) == 1:
            mapping[1] = extra.pop()
            break

    known.add(mapping[1])
    mapping[3] = (set(lengths[7][0]) - known).pop()

    known = set(mapping)
    for len_6 in lengths[6]:
        extra = set(len_6) - known
        if len(extra) == 1:
            mapping[5] = extra.pop()
            break

    mapping[2] = (set("abcdefg") - set(mapping)).pop()

    return mapping


def decode(mapping, digit_output):
    decoder = {
        ( True,  True,  True, False,  True,  True,  True): "0",
        (False, False,  True, False, False,  True, False): "1",
        ( True, False,  True,  True,  True, False,  True): "2",
        ( True, False,  True,  True, False,  True,  True): "3",
        (False,  True,  True,  True, False,  True, False): "4",
        ( True,  True, False,  True, False,  True,  True): "5",
        ( True,  True, False,  True,  True,  True,  True): "6",
        ( True, False,  True, False, False,  True, False): "7",
        ( True,  True,  True,  True,  True,  True,  True): "8",
        ( True,  True,  True,  True, False,  True,  True): "9",
    }

    reading = ""
    for digit in digit_output:
        digit_reading = tuple(segment in digit for segment in mapping)
        reading += decoder[digit_reading]

    return int(reading)


def parse_input(input_stream):
    for line in input_stream:
        signal_patterns, digit_output = line.split("|")
        yield signal_patterns.split(), digit_output.split()


def solve(input_stream):
    total = 0
    for signal_patterns, digit_output in parse_input(input_stream):
        mapping = decipher(signal_patterns)
        reading = decode(mapping, digit_output)

        total += reading

    return total


if __name__ == "__main__":
    answer = solve(fileinput.input())
    pprint(answer)
