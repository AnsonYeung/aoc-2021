#!/usr/bin/env python3
import sys
data = sys.stdin.read().split('\n')[:-1]

print(len(data))

map = []
for i in range(1000):
    map.append([0] * 1000)

for d in data:
    x1 = int(d.split(',', 1)[0])
    y1 = int(d.split(',', 1)[1].split(' ')[0])
    x2 = int(d.split('-> ', 1)[1].split(',')[0])
    y2 = int(d.split('-> ', 1)[1].split(',')[1])
    if x1 == x2 and y1 == y2:
        map[x1][y1] += 1
    elif x1 == x2:
        for i in range(min(y1, y2), max(y1, y2) + 1):
            map[x1][i] += 1
    elif y1 == y2:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            map[i][y1] += 1
    else:
        if x1 > x2:
            x1, y1, x2, y2 = x2, y2, x1, y1
        delta = 1 if y2 > y1 else -1
        print(x1, y1, x2, y2, delta)
        for i in range(x2 - x1 + 1):
            map[x1 + i][y1 + i * delta] += 1

total = 0
for r in map:
    for c in r:
        if c > 1:
            total += 1

print(total)
