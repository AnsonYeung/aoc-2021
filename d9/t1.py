#!/usr/bin/env python3
import sys
data = sys.stdin.read().split('\n')[:-1]

print(len(data))
print(len(data[0]))

data = [[int(j) for j in i] for i in data]

s = 0

for i in range(100):
    for j in range(100):
        if i - 1 >= 0 and data[i][j] >= data[i - 1][j]: continue
        if i + 1 < 100 and data[i][j] >= data[i + 1][j]: continue
        if j - 1 >= 0 and data[i][j] >= data[i][j - 1]: continue
        if j + 1 < 100 and data[i][j] >= data[i][j + 1]: continue
        s += data[i][j] + 1
print(s)
        


