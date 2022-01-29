#!/usr/bin/env python3
import fileinput
from pprint import pprint
from grid import Coord, Grid


def parse_input(input_stream):
    for line in input_stream:
        yield map(lambda n: int(n, 10), line.strip())


def check_neighbours(coord, heightmap):
    if coord.y >= 0 and coord.x >= 0:
        try:
            value = heightmap[coord]
        except IndexError:
            pass
        else:
            if value < 9:
                yield coord

                heightmap[coord] = 9

                yield from check_neighbours(Coord(coord.x - 1, coord.y), heightmap)
                yield from check_neighbours(Coord(coord.x + 1, coord.y), heightmap)
                yield from check_neighbours(Coord(coord.x, coord.y - 1), heightmap)
                yield from check_neighbours(Coord(coord.x, coord.y + 1), heightmap)


def find_basins(input_stream):
    heightmap = Grid.from_iterable(parse_input(input_stream))

    basins = []
    for coord in heightmap.itercoords():
        new_basin = set(check_neighbours(coord, heightmap))
        if new_basin:
            basins.append(new_basin)

    return basins


def solve(input_stream):
    basin_sizes = tuple(sorted((len(basin) for basin in find_basins(input_stream)), reverse=True))
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


if __name__ == "__main__":
    answer = solve(fileinput.input())
    pprint(answer)
