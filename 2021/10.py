#!/usr/bin/env python3
import fileinput
from pprint import pprint


def find_corrupted(line):
    mapping = {
        "]": "[",
        "}": "{",
        ")": "(",
        ">": "<",
    }

    stack = []
    for char in line:
        if char in mapping.values():
            stack.append(char)
        elif mapping[char] == stack[-1]:
            stack.pop()
        else:
            return char


def parse_input(input_stream):
    for line in input_stream:
        yield find_corrupted(line.strip())


def solve(input_stream):
    scores = {
        None: 0,
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    return sum(scores[char] for char in parse_input(input_stream))


if __name__ == "__main__":
    answer = solve(fileinput.input())
    pprint(answer)
