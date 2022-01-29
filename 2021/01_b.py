#!/usr/bin/env python3
import fileinput
from collections import deque


def solve(input_stream):
    last_seen = None
    increments = 0

    sliding_windows = deque()

    for line in input_stream:
        measurement = int(line)

        for entry in sliding_windows:
            entry.append(measurement)

        sliding_windows.append([measurement])

        if len(sliding_windows[0]) == 3:
            current_value = sum(sliding_windows.popleft())

            if last_seen is not None and current_value > last_seen:
                increments += 1

            last_seen = current_value

    return increments


if __name__ == "__main__":
    print(solve(fileinput.input()))
