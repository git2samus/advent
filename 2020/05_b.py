#!/usr/bin/env python3
import fileinput

def parse_row(data):
    return int(''.join('1' if c == 'B' else '0' for c in data), 2)

def parse_col(data):
    return int(''.join('1' if c == 'R' else '0' for c in data), 2)

def calc_id(line):
    row_data, col_data = line[0:7], line[7:10]

    row, col = parse_row(row_data), parse_col(col_data)
    return row * 8 + col


prev = None
for seat_id in sorted(calc_id(line) for line in fileinput.input()):
    if prev and prev != seat_id - 1:
        print(seat_id - 1)
        break

    prev = seat_id
