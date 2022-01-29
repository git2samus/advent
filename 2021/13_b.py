#!/usr/bin/env python3
import fileinput
#from pprint import pprint
from grid import Coord, Grid


def parse_input(input_stream):
    coords, folds = set(), []

    first_block = True
    for line in input_stream:
        line = line.strip()

        if first_block:
            if not line:
                first_block = False
                continue

            coords.add(
                Coord(*map(int, line.split(",")))
            )
        else:
            direction, position = line.split("=")
            folds.append(
                (direction[-1], int(position))
            )

    return coords, folds


def fold_paper(input_stream):
    coords, folds = parse_input(input_stream)

    for direction, position in folds:
        new_coords = set()
        for coord in coords:
            if direction == "x":
                if coord.x > position:
                    new_coords.add(
                        Coord(position - (coord.x - position), coord.y)
                    )
                else:
                    new_coords.add(coord)
            else:
                if coord.y > position:
                    new_coords.add(
                        Coord(coord.x, position - (coord.y - position))
                    )
                else:
                    new_coords.add(coord)

        coords = new_coords

    return coords


def solve(input_stream):
    coords = fold_paper(input_stream)

    width = max(coord.x for coord in coords)
    height = max(coord.y for coord in coords)

    paper = Grid(width+1, height+1, " ")
    for coord in coords:
        paper[coord] = "#"

    return paper


if __name__ == "__main__":
    paper = solve(fileinput.input())
    for row in paper.rows:
        print("".join(row))
