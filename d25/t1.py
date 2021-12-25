#!/usr/bin/env pypy3
from sys import stdin, exit
from copy import *
from heapq import *
from collections import *
from itertools import *
from math import *

data = stdin.read().split('\n')[:-1]

print(data)
count = 0
while True:
    lastdata = data
    data = [['.' for _ in data[0]] for _ in data]
    for i, row in enumerate(lastdata):
        for j, ent in enumerate(row):
            if ent == '>':
                n = (j + 1) % len(data[0])
                if lastdata[i][n] == '.':
                    data[i][n] = '>'
                else:
                    data[i][j] = '>'
            elif ent == 'v':
                data[i][j] = 'v'
    tdata = data
    data = [['.' for _ in data[0]] for _ in data]
    for i, row in enumerate(tdata):
        for j, ent in enumerate(row):
            if ent == 'v':
                n = (i + 1) % len(data)
                if tdata[n][j] == '.':
                    data[n][j] = 'v'
                else:
                    data[i][j] = 'v'
            elif ent == '>':
                data[i][j] = '>'
    count += 1
    for r in data:
        for c in r:
            pass
            #print(c,end='')
        #print()
    #print(count)
    if lastdata == data:
        print(count)
        break



