#!/usr/bin/env python3
import sys
from collections import *
data = sys.stdin.read().split('\n')[:-1]

newpix = data[0]
print(newpix)
print(len(newpix))

image = deque(deque(1 if pix == '#' else 0 for pix in row) for row in data[2:])
imagemap = {}
for i, row in enumerate(data[2:]):
    for j, pix in enumerate(row):
        if pix == '#':
            imagemap[(i, j)] = 1

def calPixel(x, y):
    global imagemap
    res = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            imagemap.setdefault((x + i, y + j), 0)
            res = res * 2 + imagemap[(x + i, y + j)]
    return newpix[res] == '#'

for _ in range(50):
    newmap = {}
    for i in range(-200, 300):
        for j in range(-200, 300):
            newmap[(i, j)] = calPixel(i, j)
    imagemap = newmap


newmappix = 0
for i in range(-100, 200):
    for j in range(-100, 200):
        if imagemap[(i, j)] == 1:
            newmappix += 1
        if imagemap[(i, j)] == 1:
            print('#', end='')
        else:
            print('.', end='')
    print()
print(newmappix)
