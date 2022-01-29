#!/usr/bin/env python3
import fileinput
#from pprint import pprint


def read_blocks(input_stream):
    accumulator = []

    for line in input_stream:
        line = line.strip()

        if not line:
            yield accumulator
            accumulator = []
            continue

        accumulator.append(line)

    yield accumulator


def parse_input(input_stream):
    blocks = read_blocks(input_stream)

    draws = tuple(map(int, next(blocks).pop().split(",")))

    boards = []
    for block in blocks:
        board = tuple(
            tuple(
                [int(x), False] for x in line.split()
            ) for line in block
        )
        boards.append(board)

    return draws, boards


def check_board(board):
    return any(
        all(board[y][x][1] for x in range(len(board)))
        for y in range(len(board))
    ) or any(
        all(board[y][x][1] for y in range(len(board)))
        for x in range(len(board))
    )


def mark_board(draw, board):
    for row in board:
        for col in row:
            if col[0] == draw:
                col[1] = True


def solve(input_stream):
    draws, boards = parse_input(input_stream)

    for draw in draws:
        for board in boards:
            mark_board(draw, board)

            if check_board(board):
                sum_board = 0
                for row in board:
                    for col in row:
                        if not col[1]:
                            sum_board += col[0]

                return draw * sum_board


if __name__ == "__main__":
    print(solve(fileinput.input()))
