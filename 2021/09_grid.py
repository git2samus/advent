#!/usr/bin/env python3
import fileinput
from pprint import pprint
from grid import Coord, Grid


def parse_input(input_stream):
    for line in input_stream:
        yield map(int, line.strip())


def find_lowest(input_stream):
    heightmap = Grid.from_iterable(parse_input(input_stream))

    for coord in heightmap.itercoords():
        value = heightmap[coord]

        minimum = True

        if coord.x - 1 >= 0:
            minimum = minimum and value < heightmap[Coord(coord.x - 1, coord.y)]

        if coord.x + 1 < heightmap.width:
            minimum = minimum and value < heightmap[Coord(coord.x + 1, coord.y)]

        if coord.y - 1 >= 0:
            minimum = minimum and value < heightmap[Coord(coord.x, coord.y - 1)]

        if coord.y + 1 < heightmap.height:
            minimum = minimum and value < heightmap[Coord(coord.x, coord.y + 1)]

        if minimum:
            yield value


def solve(input_stream):
    return sum(1 + minimum for minimum in find_lowest(input_stream))


if __name__ == "__main__":
    answer = solve(fileinput.input())
    pprint(answer)
