#!/usr/bin/env python3
import fileinput
from pprint import pprint


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
                tuple(map(int, line.split(",")))
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
                if coord[0] > position:
                    new_coords.add(
                        (position - (coord[0] - position), coord[1])
                    )
                else:
                    new_coords.add(coord)
            else:
                if coord[1] > position:
                    new_coords.add(
                        (coord[0], position - (coord[1] - position))
                    )
                else:
                    new_coords.add(coord)

        coords = new_coords
        break

    return coords


def solve(input_stream):
    return len(fold_paper(input_stream))


if __name__ == "__main__":
    answer = solve(fileinput.input())
    pprint(answer)
