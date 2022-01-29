#!/usr/bin/env python3
import fileinput
from pprint import pprint


def parse_input(input_stream):
    for line in input_stream:
        yield map(lambda n: int(n, 10), line.strip())


def find_lowest(input_stream):
    heightmap = list(list(line) for line in parse_input(input_stream))

    for row_i in range(len(heightmap)):
        row = heightmap[row_i]
        for col_i in range(len(row)):
            value = row[col_i]

            minimum = True

            if col_i - 1 >= 0:
                minimum = minimum and value < row[col_i - 1]

            try:
                minimum = minimum and value < row[col_i + 1]
            except IndexError:
                pass

            if row_i - 1 >= 0:
                minimum = minimum and value < heightmap[row_i - 1][col_i]

            try:
                minimum = minimum and value < heightmap[row_i + 1][col_i]
            except IndexError:
                pass

            if minimum:
                yield value


def solve(input_stream):
    return sum(1 + minimum for minimum in find_lowest(input_stream))


if __name__ == "__main__":
    answer = solve(fileinput.input())
    pprint(answer)
