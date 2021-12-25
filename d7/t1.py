#!/usr/bin/env python3
import sys
data = sys.stdin.read().split('\n')[:-1]
data = [int(x) for x in data[0].split(',')]
print(data)

data = sorted(data)
print(len(data))
t = data[len(data) // 2]

print(sum(abs(x - t) for x in data))

