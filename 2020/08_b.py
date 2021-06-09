#!/usr/bin/env python3
import fileinput
from collections import namedtuple

Op = namedtuple('Op', ('op', 'arg'))

code = []
for line in fileinput.input():
    op, arg = line.split()
    code.append(Op(op, int(arg)))


def run(code):
    acc, ptr = 0, 0
    seen = set()

    while 0 <= ptr < len(code):
        if ptr in seen:
            break

        seen.add(ptr)
        instr = code[ptr]

        if instr.op == 'acc':
            acc += instr.arg

        if instr.op == 'jmp':
            ptr += instr.arg
        else:
            ptr += 1

    if ptr == len(code):
        return acc


for lineno in range(len(code)):
    instr = code[lineno]

    if instr.op in ('jmp', 'nop'):
        test_code = code.copy()

        test_code[lineno] = Op('nop' if instr.op == 'jmp' else 'jmp', instr.arg)
        res = run(test_code)

        if res is not None:
            print(res)
