#!/usr/bin/env python3
import fileinput
from pprint import pprint
from collections import defaultdict


def parse_input(input_stream):
    for line in input_stream:
        yield line.strip().split("-")


def tracepath(path, tunnels, small_cave=True):
    current_cave = path[-1]

    if current_cave == "end":
        yield path
    else:
        for next_cave in tunnels[current_cave]:
            if next_cave.islower():
                if next_cave not in path:
                    yield from tracepath(path + [next_cave], tunnels, small_cave)
                elif small_cave and next_cave not in {"start", "end"}:
                    yield from tracepath(path + [next_cave], tunnels, False)
            else:
                yield from tracepath(path + [next_cave], tunnels, small_cave)


def solve(input_stream):
    tunnels = defaultdict(set)

    for cave_a, cave_b in parse_input(input_stream):
        tunnels[cave_a].add(cave_b)
        tunnels[cave_b].add(cave_a)

    #pprint(tunnels)

    paths = list(tracepath(["start"], tunnels))
    #pprint(paths)

    return len(paths)


if __name__ == "__main__":
    answer = solve(fileinput.input())
    pprint(answer)
