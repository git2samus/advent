#!/usr/bin/env python3
import fileinput
from pprint import pprint


def parse_input(input_stream):
    for line in input_stream:
        yield list(map(int, line.strip()))


def cascade(coord, state):
    try:
        state[coord[0]][coord[1]] += 1
    except IndexError:
        return

    if state[coord[0]][coord[1]] == 10:
        for row_i in (coord[0] - 1, coord[0], coord[0] + 1):
            for col_i in (coord[1] - 1, coord[1], coord[1] + 1):
                if all((
                    row_i >= 0, col_i >= 0,
                    (row_i, col_i) != coord
                )):
                    cascade((row_i, col_i), state)


def solve(input_stream, iterations):
    state = list(parse_input(input_stream))

    iteration = 1
    while True:

        for row_i in range(len(state)):
            row = state[row_i]

            for col_i in range(len(row)):
                cascade((row_i, col_i), state)

        for row_i in range(len(state)):
            row = state[row_i]

            for col_i in range(len(row)):
                if state[row_i][col_i] >= 10:
                    state[row_i][col_i] = 0

        if all(cell == 0 for row in state for cell in row):
            return iteration

        iteration += 1


if __name__ == "__main__":
    answer = solve(fileinput.input(), 100)
    pprint(answer)
