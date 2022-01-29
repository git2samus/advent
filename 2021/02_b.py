#!/usr/bin/env python3
import fileinput


def solve(input_stream):
    position, depth, aim = 0, 0, 0

    for line in input_stream:
        tokens = line.split()
        command, distance = tokens[0], int(tokens[1])

        if command == "forward":
            position += distance
            depth += aim * distance
        elif command == "down":
            aim += distance
        elif command == "up":
            aim -= distance

    return position, depth


if __name__ == "__main__":
    position, depth = solve(fileinput.input())
    print(position * depth)
