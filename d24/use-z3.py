#!/usr/bin/env python3
from sys import stdin, exit
from copy import *
from heapq import *
from collections import *
from itertools import *
from math import *
from z3 import *

data = open("input.txt").read().strip().split('\n')
#data = stdin.read().split('\n')[:-1]

def run(inp):
    var = {'x': IntVal(0), 'y': IntVal(0), 'z': IntVal(0), 'w': IntVal(0)}
    #var = {'x': 0, 'y': 0, 'z': 0, 'w': 0}
    cur = 0
    for line in data:
        p = line.split(' ')
        if p[0] == 'inp':
            var[p[1]] = inp[cur]
            #var[p[1]] = int(inp[cur])
            cur += 1
        else:
            if p[2] in var:
                op2 = var[p[2]]
            else:
                op2 = int(p[2])
            if p[0] == 'add':
                var[p[1]] += op2
            elif p[0] == 'mul':
                var[p[1]] *= op2
            elif p[0] == 'div':
                var[p[1]] = simplify(If(var[p[1]] < 0, -((-var[p[1]]) / op2), var[p[1]] / op2))
                #if var[p[1]] < 0:
                #    var[p[1]] = -((-var[p[1]]) // op2)
                #else:
                #    var[p[1]] = var[p[1]] // op2
            elif p[0] == 'mod':
                var[p[1]] %= op2
            elif p[0] == 'eql':
                var[p[1]] = If(var[p[1]] == op2, 1, 0)
                #var[p[1]] = 1 if var[p[1]] == op2 else 0
    return var['z']

magicIn = [Int(f'in{i}') for i in range(14)]
s = Solver()
for i in magicIn:
    s.add(i >= 1)
    s.add(i <= 9)
x = run(magicIn)
x = simplify(x)
print(simplify(x == 0))
s.add(x == 0)

print(s)
print(s.check())

while s.check() == sat:
    m = s.model()
    print(m)


