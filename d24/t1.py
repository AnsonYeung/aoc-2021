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

notok = set()
mn = 100000000000000

def dfs(ln=0, reg=(0, 0, 0, 0)):
    global mn
    if (ln, reg) in notok:
        return -1
    var = {'x': reg[0], 'y': reg[1], 'z': reg[2], 'w': reg[3]}
    for i in range(ln, len(data)):
        p = data[i].split(' ')
        if p[0] == 'inp':
            for testin in range(9, 0, -1):
                var[p[1]] = testin
                ret = dfs(i + 1, (var['x'], var['y'], var['z'], var['w']))
                if ret != -1:
                    print(testin)
                    return ret
            notok.add((ln, reg))
            #print((ln, reg))
            return -1
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
    #print((ln, reg))
    if var['z'] < mn:
        mn = var['z']
        print('omg! ', mn)
    if var['z'] != 0:
        notok.add((ln, reg))
        return -1
    return 0

print(dfs())

x = '9'*14
mn = 100000000000000000000000
while True:
    # x = input("input val to run> ")
    r = run(x)
    if r == 0:
        break
    if r < 1000000:
        mn = r
        print(x, r)
    if r < mn:
        mn = r
        print(x, r)
    x = str(int(x) - 1)
    while any(c == '0' for c in x):
        x = str(int(x) - 1)
print(x)

