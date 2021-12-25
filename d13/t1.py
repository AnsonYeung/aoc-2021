#!/usr/bin/env python3
import sys
data = sys.stdin.read().split('\n')[:-1]

print(len(data))

paper = [[False for i in range(2000)] for j in range(2000)]

i = 0
for i in range(len(data)):
    if data[i] == '': break
    coord = data[i].split(',')
    paper[int(coord[0])][int(coord[1])] = True

i += 1

inst = data[i].split('=')
loc = int(inst[1])
di = inst[0][-1]
for j in range(loc + 1, 2000):
    for k in range(2000):
        paper[loc - (j - loc)][k] |= paper[j][k]
        paper[j][k] = False

print(sum(row.count(True) for row in paper))
