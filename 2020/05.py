#!/usr/bin/env python3
import fileinput

def parse_row(data):
    return int(''.join('1' if c == 'B' else '0' for c in data), 2)

def parse_col(data):
    return int(''.join('1' if c == 'R' else '0' for c in data), 2)


max_id = 0

for line in fileinput.input():
    row_data, col_data = line[0:7], line[7:10]

    row, col = parse_row(row_data), parse_col(col_data)
    seat_id = row * 8 + col

    max_id = max(max_id, seat_id)

print(max_id)
