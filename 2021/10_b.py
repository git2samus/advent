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
    reverse_mapping = dict((v, k) for k, v in mapping.items())

    stack = []
    for char in line:
        if char in mapping.values():
            stack.append(char)
        elif mapping[char] == stack[-1]:
            stack.pop()
        else:
            return None

    stack.reverse()
    return [reverse_mapping[char] for char in stack]


def parse_input(input_stream):
    for line in input_stream:
        yield find_corrupted(line.strip())


def solve(input_stream):
    scores = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }

    results = []
    for line in parse_input(input_stream):
        if line:
            score = 0
            for char in line:
                score *= 5
                score += scores[char]

            results.append(score)

    results.sort()
    return results[len(results) // 2]


if __name__ == "__main__":
    answer = solve(fileinput.input())
    pprint(answer)
