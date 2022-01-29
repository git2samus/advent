#!/usr/bin/env python3
import fileinput
from pprint import pprint
from grid import Coord, Grid


def parse_input(input_stream):
    for line in input_stream:
        yield map(int, line.strip())


def cascade(coord, state):
    state[coord] += 1

    if state[coord] == 10:
        for delta_y in (-1, 0, 1):
            for delta_x in (-1, 0, 1):
                new_coord = Coord(coord.x + delta_x, coord.y + delta_y)

                if all((
                    0 <= new_coord.y < state.height,
                    0 <= new_coord.x < state.width,
                    new_coord != coord
                )):
                    cascade(new_coord, state)


def solve(input_stream, iterations):
    state = Grid.from_iterable(parse_input(input_stream))

    blinks = 0
    for iteration in range(iterations):

        for coord in state.itercoords():
            cascade(coord, state)

        for coord in state.itercoords():
            if state[coord] >= 10:
                state[coord] = 0
                blinks += 1

    return blinks


if __name__ == "__main__":
    answer = solve(fileinput.input(), 100)
    pprint(answer)
