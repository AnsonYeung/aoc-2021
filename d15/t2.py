#!/usr/bin/env python3
import sys
data = sys.stdin.read().split('\n')[:-1]
data = [[int(x) for x in row] for row in data]
print(len(data))
print(len(data[0]))
N = 500
M = 100
ndata = []
for i in range(N):
    ndata.append([])
    for j in range(N):
        ndata[i].append((data[i % M][j % M] + i // M + j // M - 1) % 9 + 1)
data = ndata
print(len(ndata))
print(len(ndata[0]))

risk = [[100000000000 for x in range(N)] for y in range(N)]

risk[0][0] = 0

for t in range(N * N):
    nrisk = [row.copy() for row in risk]
    for x in range(N):
        for y in range(N):
            if x > 0: nrisk[x][y] = min(nrisk[x][y], nrisk[x - 1][y] + data[x][y])
            if x < N-1: nrisk[x][y] = min(nrisk[x][y], nrisk[x + 1][y] + data[x][y])
            if y > 0: nrisk[x][y] = min(nrisk[x][y], nrisk[x][y - 1] + data[x][y])
            if y < N-1: nrisk[x][y] = min(nrisk[x][y], nrisk[x][y + 1] + data[x][y])

    print(nrisk[N-1][N-1])

    if nrisk == risk: break
    risk = nrisk
