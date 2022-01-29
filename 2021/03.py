#!/usr/bin/env python3
import fileinput


def solve(input_stream):
    counts = []

    for line in input_stream:
        for pos, bit in enumerate(line.strip()):
            try:
                counts[pos]
            except IndexError:
                counts.append(0)

            counts[pos] += 1 if bit == "1" else -1

    gamma = "".join("1" if bit > 0 else "0" for bit in counts)
    epsilon = "".join("0" if bit > 0 else "1" for bit in counts)

    return int(gamma, 2), int(epsilon, 2)


if __name__ == "__main__":
    gamma, epsilon = solve(fileinput.input())
    print(gamma * epsilon)
