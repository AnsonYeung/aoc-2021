#!/usr/bin/env python3
import sys
data = sys.stdin.read().split('\n')[:-1]

print(len(data))
print(len(data[0]))

data = [[int(j) for j in i] for i in data]

visited = [[False] * 100 for _ in data]

def valid(c):
    return c[0] >= 0 and c[0] < 100 and c[1] >= 0 and c[1] < 100

def dfs(c, p):
    if visited[c[0]][c[1]]: return 0
    if data[c[0]][c[1]] == 9: return 0
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited[c[0]][c[1]] = True
    total = 0
    for d in dirs:
        dest = (c[0] + d[0], c[1] + d[1])
        if valid(dest) and dest != p:
            total += dfs(dest, c)
    return total + 1


s = 0

low = []
for i in range(100):
    for j in range(100):
        if i - 1 >= 0 and data[i][j] >= data[i - 1][j]: continue
        if i + 1 < 100 and data[i][j] >= data[i + 1][j]: continue
        if j - 1 >= 0 and data[i][j] >= data[i][j - 1]: continue
        if j + 1 < 100 and data[i][j] >= data[i][j + 1]: continue
        low.append((i, j))

sizes = []

for l in low:
    sizes.append(dfs(l, l))

print(sizes)
sizes = sorted(sizes)
print(sizes)
print(sizes[-1] * sizes[-2] * sizes[-3])
print(30*27*27)
