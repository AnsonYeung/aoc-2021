#!/usr/bin/env pypy3
from sys import stdin, exit
from copy import *
from heapq import *
from collections import *
from itertools import *
from math import *
#from z3 import *

data = open("input.txt").read().strip().split('\n')
#data = stdin.read().split('\n')[:-1]

def run(inp):
    var = {'x': 0, 'y': 0, 'z': 0, 'w': 0}
    cur = 0
    for line in data:
        p = line.split(' ')
        if p[0] == 'inp':
            var[p[1]] = int(inp[cur])
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
                if var[p[1]] < 0:
                    var[p[1]] = -((-var[p[1]]) // op2)
                else:
                    var[p[1]] = var[p[1]] // op2
            elif p[0] == 'mod':
                var[p[1]] %= op2
            elif p[0] == 'eql':
                var[p[1]] = 1 if var[p[1]] == op2 else 0
    return var['z']

x = '9'*14
mn = 100000000000000000000000
while True:
    x = input("input val to run> ").strip()
    r = run(x)
    print(x, r)
    if r == 0:
        break
    if r < 1000000:
        print('impressive!')
        mn = r
        print(x, r)
    if r < mn:
        print('new record!')
        mn = r
        print(x, r)
    x = str(int(x) - 1)
    while any(c == '0' for c in x):
        x = str(int(x) - 1)
print(x)

