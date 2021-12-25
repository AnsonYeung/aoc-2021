#!/usr/bin/env python3
import sys
data = sys.stdin.read().split('\n')[:-1]

print(len(data))

dots: 'set[tuple[int, int]]' = set()

i = 0
for i in range(len(data)):
    if data[i] == '': break
    coord = data[i].split(',')
    dots.add((int(coord[0]), int(coord[1])))

i += 1

while i < len(data):
    inst = data[i].split('=')
    loc = int(inst[1])
    di = inst[0][-1]
    print(loc)
    newdots: 'set[tuple[int, int]]' = set()
    for dot in dots:
        fst, snd = dot[0], dot[1]
        if di == 'y': fst, snd = snd, fst
        if fst > loc:
            fst = loc * 2 - fst
        if di == 'y': fst, snd = snd, fst
        newdots.add((fst, snd))
    dots = newdots
    i += 1

for j in range(max(dot[1] for dot in dots) + 1):
    for i in range(max(dot[0] for dot in dots) + 1):
        print('#' if (i, j) in dots else ' ', end='')
    print()



