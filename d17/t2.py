#!/usr/bin/env python3
import sys
data = sys.stdin.read().split('\n')[:-1]

s = data[0].split('x=')[1].split('..')
x1 = int(s[0])
y2 = int(s[2])
s = s[1].split(', y=')
x2 = int(s[0])
y1 = int(s[1])
print(x1, x2, y1, y2)
minx = 100
maxx = 0
sumx = 0
for i in range(1, 100):
    sumx += i
    if x1 <= sumx <= x2:
        if i < minx:
            minx = i
        if i > maxx:
            maxx = i

print(minx, maxx)
aMax = 0
count = 0
for vx in range(minx, x2+1):
    for vy in range(-189, 189):
        v = [vx, vy]
        pos = [0, 0]
        hiY = 0
        while pos[0] <= x2:
            pos[0] += v[0]
            pos[1] += v[1]
            if v[0] > 0:
                v[0] -= 1
            v[1] -= 1
            if pos[1] > hiY:
                hiY = pos[1]
            if pos[1] < y1:
                break
            if x1 <= pos[0] <= x2 and y1 <= pos[1] <= y2:
                print(vx, vy, hiY)
                count += 1
                if hiY > aMax:
                    aMax = hiY
                break
print(aMax)
print(count)
