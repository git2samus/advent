#!/usr/bin/env python3
import fileinput
from pprint import pprint


def parse_input(input_stream):
    for line in input_stream:
        yield map(lambda n: int(n, 10), line.strip())


def check_neighbours(coord, heightmap):
    row_i, col_i = coord

    if row_i >= 0 and col_i >= 0:
        try:
            value = heightmap[row_i][col_i]
        except IndexError:
            pass
        else:
            if value < 9:
                yield coord

                heightmap[row_i][col_i] = 9

                yield from check_neighbours((row_i - 1, col_i), heightmap)
                yield from check_neighbours((row_i + 1, col_i), heightmap)
                yield from check_neighbours((row_i, col_i - 1), heightmap)
                yield from check_neighbours((row_i, col_i + 1), heightmap)


def find_basins(input_stream):
    heightmap = list(list(line) for line in parse_input(input_stream))

    basins = []
    for row_i in range(len(heightmap)):
        for col_i in range(len(heightmap[row_i])):
            coord = (row_i, col_i)

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
