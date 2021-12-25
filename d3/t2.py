#!/usr/bin/env python3
import sys
i = sys.stdin.read().split('\n')[:-1]


print(len(i))

print(len(i[0]))

data = i
data2 = i.copy()
curbit = 0
while len(data) != 1:
    count = 0
    for x in data:
        if x[curbit] == '1':
            count += 1
    if len(data) - count > count:
        keep = '0'
    else:
        keep = '1'
    ndata = []
    for x in data:
        if x[curbit] == keep:
            ndata.append(x)
    data = ndata
    curbit = (curbit + 1)

print(data)
ans1 = int(data[0], 2)
data = data2
print(len(data))
curbit = 0
while len(data) != 1:
    count = 0
    for x in data:
        if x[curbit] == '1':
            count += 1
    if len(data) - count <= count:
        keep = '0'
    else:
        keep = '1'
    ndata = []
    for x in data:
        if x[curbit] == keep:
            ndata.append(x)
    data = ndata
    curbit = (curbit + 1)
print(data)
print(int(data[0], 2) * ans1)
