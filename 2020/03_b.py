#!/usr/bin/env python3
import fileinput, operator
from collections import namedtuple
from functools import reduce

Coord = namedtuple('Coord', ('x', 'y'))

tree_map = [line.strip() for line in fileinput.input()]

def calc(slope):
    pos, trees = Coord(0, 0), 0

    while pos.y < len(tree_map):
        if tree_map[pos.y][pos.x] == '#':
            trees += 1

        pos = Coord((pos.x + slope.x) % len(tree_map[0]), pos.y + slope.y)

    return trees


slopes = (
    Coord(1, 1),
    Coord(3, 1),
    Coord(5, 1),
    Coord(7, 1),
    Coord(1, 2),
)

print(reduce(operator.mul, map(calc, slopes)))
