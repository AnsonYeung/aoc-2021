#!/usr/bin/env python3
import sys
import typing
data = sys.stdin.read() # type: ignore

Coord = typing.Tuple[int, int, int]
ScannerData = typing.Set[Coord]

data: typing.List[ScannerData] = [set(tuple(int(pos) for pos in coord.split(',')) for coord in beacon.rstrip().split('\n')[1:]) for beacon in data.split('\n\n')] # type: ignore

def rotateX(a) -> Coord:
    return a[0], -a[2], a[1]

def rotateY(a) -> Coord:
    return a[2], a[1], -a[0]

def rotateZ(a) -> Coord:
    return -a[1], a[0], a[2]

def rotateXn(a, n) -> Coord:
    for i in range(n):
        a = rotateX(a)
    return a

def rotateYn(a, n) -> Coord:
    for i in range(n):
        a = rotateY(a)
    return a

def rotateZn(a, n) -> Coord:
    for i in range(n):
        a = rotateZ(a)
    return a

def addData(a, b) -> typing.Tuple[int, int, int, int, int, int]:

    v1 = (1, 0, 0)
    v2 = (0, 1, 0)

    v1 = rotateXn(v1, a[3])
    v1 = rotateYn(v1, a[4])
    v1 = rotateZn(v1, a[5])
    v1 = rotateXn(v1, b[3])
    v1 = rotateYn(v1, b[4])
    v1 = rotateZn(v1, b[5])

    v2 = rotateXn(v2, a[3])
    v2 = rotateYn(v2, a[4])
    v2 = rotateZn(v2, a[5])
    v2 = rotateXn(v2, b[3])
    v2 = rotateYn(v2, b[4])
    v2 = rotateZn(v2, b[5])

    b = rotateZn(b, 4 - a[5])
    b = rotateYn(b, 4 - a[4])
    b = rotateXn(b, 4 - a[3])

    a1 = (1, 0, 0)
    a2 = (0, 1, 0)
    for xrot in range(4):
        for yrot in range(4):
            for zrot in range(4):
                if a1 == v1 and a2 == v2:
                    print(a[0] + b[0], a[1] + b[1], a[2] + b[2], xrot, yrot, zrot)
                    return a[0] + b[0], a[1] + b[1], a[2] + b[2], xrot, yrot, zrot
                a1 = rotateZ(a1)
                a2 = rotateZ(a2)
            a1 = rotateY(a1)
            a2 = rotateY(a2)
        a1 = rotateX(a1)
        a2 = rotateX(a2)
    raise Exception("Impossible configuration")

def addcoord(a: Coord, b: Coord) -> Coord:
    return a[0] + b[0], a[1] + b[1], a[2] + b[2]

def subcoord(a: Coord, b: Coord) -> Coord:
    return a[0] - b[0], a[1] - b[1], a[2] - b[2]

def tryMerge(scan1: ScannerData, scan2: ScannerData) -> typing.Tuple[bool, int, int, int, int, int, int]:
    for xrot in range(4):
        for yrot in range(4):
            for zrot in range(4):
                for d1 in scan1:
                    for d2 in scan2:
                        count = 0
                        for c2 in scan2:
                            coordT = (c2[0] - d2[0] + d1[0], c2[1] - d2[1] + d1[1], c2[2] - d2[2] + d1[2])
                            if coordT in scan1:
                                count += 1
                        if count >= 12:
                            print('merge success')
                            rel: Coord = subcoord(d1, d2)
                            for i in range(4-zrot): rel = rotateZ(rel)
                            for i in range(4-yrot): rel = rotateY(rel)
                            for i in range(4-xrot): rel = rotateX(rel)
                            return True, *rel, xrot, yrot, zrot
                scan1 = set(rotateZ(pos) for pos in scan1)
            scan1 = set(rotateY(pos) for pos in scan1)
        scan1 = set(rotateX(pos) for pos in scan1)
    return False, 0, 0, 0, 0, 0, 0

known = [True, *[False for i in range(len(data) - 1)]]
mergeData: typing.List[typing.Tuple[int, int, int, int, int, int]] = [(0, 0, 0, 0, 0, 0) for i in range(len(data))]
allBeacon = data[0]

def dfs(cur):
    for i in range(len(data)):
        if not known[i]:
            success, *result = tryMerge(data[cur], data[i])
            if success:
                print(i)
                known[i] = True
                print(result)
                mergeData[i] = addData(mergeData[cur], tuple(result))
                print(mergeData[i])
                print(mergeData)
                datai = data[i]
                for j in range(4-mergeData[i][5]):
                    datai = [rotateZ(pos) for pos in datai]
                for j in range(4-mergeData[i][4]):
                    datai = [rotateY(pos) for pos in datai]
                for j in range(4-mergeData[i][3]):
                    datai = [rotateX(pos) for pos in datai]
                for j in datai:
                    allBeacon.add((j[0] + mergeData[i][0], j[1] + mergeData[i][1], j[2] + mergeData[i][2]))
                dfs(i)

dfs(0)

# while not all(known):
#     for i in range(len(data)):
#         if not known[i]:
#             success, *result = tryMerge(allBeacon, data[i])
#             if success:
#                 print(i)
#                 known[i] = True
#                 mergeData[i] = tuple(result) # type: ignore
#                 datai = data[i]
#                 for j in range(4-mergeData[i][5]):
#                     datai = [rotateZ(pos) for pos in datai]
#                 for j in range(4-mergeData[i][4]):
#                     datai = [rotateY(pos) for pos in datai]
#                 for j in range(4-mergeData[i][3]):
#                     datai = [rotateX(pos) for pos in datai]
#                 for j in datai:
#                     allBeacon.add((j[0] + mergeData[i][0], j[1] + mergeData[i][1], j[2] + mergeData[i][2]))
print(known)
print(mergeData)
print(len(allBeacon))
# success, x, y, z, xrot, yrot = tryMerge(data[0], data[1])
# data1 = data[1]
# for i in range(xrot):
#     data1 = [rotateX(pos) for pos in data1]
# for i in range(yrot):
#     data1 = [rotateY(pos) for pos in data1]
# data1 = sorted([(pos[0] + x, pos[1] + y, pos[2] + z) for pos in data1])
# data0 = sorted([(pos[0], pos[1], pos[2]) for pos in data[0]])
# print('data0:',data0)
# print('data1:',data1)
