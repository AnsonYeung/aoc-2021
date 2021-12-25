#!/usr/bin/env python3
import sys
data = sys.stdin.read().split('\n')[:-1]

def rsum(a) -> int:
    try:
        return sum(a)
    except:
        return sum(rsum(i) for i in a)

parsed = []
print(len(data))

res = [[[0 for _ in range(101)] for __ in range(101)] for __ in range(101)]
print(rsum(res))

for line in data:
    val = 1 if line.startswith('on') else 0
    a = line.split('..')
    x1 = int(a[0].split('=')[1])
    x2 = int(a[1].split(',y=')[0])
    y1 = int(a[1].split(',y=')[1])
    y2 = int(a[2].split(',z=')[0])
    z1 = int(a[2].split(',z=')[1])
    z2 = int(a[3])
    # print(x1, x2, y1, y2, z1, z2)
    x1 = max(-50, x1)
    y1 = max(-50, y1)
    z1 = max(-50, z1)
    x2 = min(50, x2)
    y2 = min(50, y2)
    z2 = min(50, z2)
    # print(x1, x2, y1, y2, z1, z2)
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            for k in range(z1, z2 + 1):
                res[i][j][k] = val

print(rsum(res))
    
