#!/usr/bin/env python3
import sys
data = sys.stdin.read().split('\n')[:-1]
data = [int(x) for x in data[0].split(',')]
print(data)

data = sorted(data)
print(len(data))

mn = 100000000000000000000
for t in data:
    s = (sum((abs(x - t)) * (abs(x - t) + 1) // 2 for x in data))
    mn = min(mn, s)
print(mn)

