#!/usr/bin/env python3
import fileinput


def solve(input_stream):
    last_seen = None
    increments = 0

    for line in input_stream:
        measurement = int(line)

        if last_seen is not None and measurement > last_seen:
            increments += 1

        last_seen = measurement

    return increments


if __name__ == "__main__":
    print(solve(fileinput.input()))
