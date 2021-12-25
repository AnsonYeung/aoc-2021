#!/usr/bin/env python3
import sys
data = sys.stdin.read().split('\n')[:-1]

data = [[int(x) for x in y] for y in data]
print(len(data))
print(len(data[0]))

def valid(x, y):
    return 0 <= x < 10 and 0 <= y < 10

def flash(data, flashed, x, y):
    if data[x][y] <= 9: return 0
    if (x, y) in flashed: return 0
    flashed.add((x, y))
    total = 1
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0: continue
            if not valid(x + i, y + j): continue
            data[x + i][y + j] += 1
            total += flash(data, flashed, x + i, y + j)
    return total

step = 1
while True:
    data = [[x + 1 for x in y] for y in data]
    flashed = set()
    total = 0
    for j in range(len(data)):
        for k in range(len(data[0])):
            total += flash(data, flashed, j, k)
    if total == 100:
        print(step)
        break
    data = [[x if x <= 9 else 0 for x in y] for y in data]
    step += 1


