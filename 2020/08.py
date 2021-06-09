#!/usr/bin/env python3
import fileinput
from collections import namedtuple

Op = namedtuple('Op', ('op', 'arg'))

code = []
for line in fileinput.input():
    op, arg = line.split()
    code.append(Op(op, int(arg)))


acc, ptr = 0, 0
seen = set()

while True:
    if ptr in seen:
        print(acc)
        break

    seen.add(ptr)
    instr = code[ptr]

    if instr.op == 'acc':
        acc += instr.arg

    if instr.op == 'jmp':
        ptr += instr.arg
    else:
        ptr += 1
