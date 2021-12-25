#!/usr/bin/env python3
import sys
data = sys.stdin.read().split('\n')[:-1]
data = [[int(x) for x in row] for row in data]
print(len(data))
print(len(data[0]))

risk = [[100000000000 for x in range(100)] for y in range(100)]
risk[0][0] = 0

for t in range(10000):
    nrisk = [row.copy() for row in risk]
    for x in range(100):
        for y in range(100):
            if x > 0: nrisk[x][y] = min(nrisk[x][y], nrisk[x - 1][y] + data[x][y])
            if x < 99: nrisk[x][y] = min(nrisk[x][y], nrisk[x + 1][y] + data[x][y])
            if y > 0: nrisk[x][y] = min(nrisk[x][y], nrisk[x][y - 1] + data[x][y])
            if y < 99: nrisk[x][y] = min(nrisk[x][y], nrisk[x][y + 1] + data[x][y])

    print(nrisk[99][99])

    if nrisk == risk: break
    risk = nrisk
