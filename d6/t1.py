#!/usr/bin/env python3
import sys
data = sys.stdin.read().split('\n')[0].split(',')
data = [int(x) for x in data]
counts = [data.count(i) for i in range(9)]

for i in range(80):
    ncounts = [0] * 9
    ncounts[8] = counts[0]
    ncounts[6] = counts[0]
    for j in range(1, 9):
        ncounts[j - 1] += counts[j]
    counts = ncounts
    print(ncounts)

print(sum(counts))

