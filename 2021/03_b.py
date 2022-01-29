#!/usr/bin/env python3
import fileinput


def calculate_most_common(pos, input_stream):
    most_common = 0

    for line in input_stream:
        bit = line[pos]
        most_common += 1 if bit == "1" else -1

    return most_common


def solve_o2(input_stream):
    input_list = list(input_stream)

    pos = 0
    while True:
        most_common = calculate_most_common(pos, input_list)
        selected_bit = "1" if most_common >= 0 else "0"

        input_list = [line for line in input_list if line[pos] == selected_bit]
        if len(input_list) == 1:
            return input_list.pop()

        pos += 1


def solve_co2(input_stream):
    input_list = list(input_stream)

    pos = 0
    while True:
        most_common = calculate_most_common(pos, input_list)
        selected_bit = "0" if most_common >= 0 else "1"

        input_list = [line for line in input_list if line[pos] == selected_bit]
        if len(input_list) == 1:
            return input_list.pop()

        pos += 1


def solve(input_stream):
    input_list = [line.strip() for line in input_stream]

    o2_rating = solve_o2(input_list)
    co2_rating = solve_co2(input_list)

    return int(o2_rating, 2), int(co2_rating, 2)


if __name__ == "__main__":
    o2_rating, co2_rating = solve(fileinput.input())
    print([o2_rating, co2_rating])
    print(o2_rating * co2_rating)
