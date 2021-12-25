#!/usr/bin/env python3
import sys
from sortedcontainers import SortedSet
data = sys.stdin.read().split('\n')[:-1]

def rsum(a) -> int:
    try:
        return sum(a)
    except:
        return sum(rsum(i) for i in a)

parsed = []
print(len(data))

xcomp = SortedSet()
ycomp = SortedSet()
zcomp = SortedSet()

for line in data:
    val = 1 if line.startswith('on') else 0
    a = line.split('..')
    x1 = int(a[0].split('=')[1])
    x2 = int(a[1].split(',y=')[0])
    y1 = int(a[1].split(',y=')[1])
    y2 = int(a[2].split(',z=')[0])
    z1 = int(a[2].split(',z=')[1])
    z2 = int(a[3])
    parsed.append((val, x1, x2, y1, y2, z1, y2))
    xcomp.add(x1)
    xcomp.add(x2)
    ycomp.add(y1)
    ycomp.add(y2)
    zcomp.add(z1)
    zcomp.add(z2)

print(len(xcomp), len(ycomp), len(zcomp))
res = [[[0 for _ in range(len(zcomp))] for __ in range(len(ycomp))] for ___ in range(len(xcomp))]

