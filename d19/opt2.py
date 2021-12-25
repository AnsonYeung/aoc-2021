#!/usr/bin/env python3
import sys
import typing
import numpy

Coord = typing.List[int]
ScannerData = typing.List[Coord]
ScannerDataSet = typing.Set[Coord]

data: typing.List[ScannerData] = [[tuple(int(pos) for pos in coord.split(',')) for coord in beacon.rstrip().split('\n')[1:]] for beacon in sys.stdin.read().split('\n\n')] # type: ignore

def totuple(a):
    try:
        return tuple(totuple(i) for i in a)
    except TypeError:
        return a

# rotations
baseRotations = [
        numpy.array([
            [ 1,  0,  0],
            [ 0,  0, -1],
            [ 0,  1,  0],
        ]),
        numpy.array([
            [ 0,  0,  1],
            [ 0,  1,  0],
            [-1,  0,  0],
        ]),
        numpy.array([
            [ 0, -1,  0],
            [ 1,  0,  0],
            [ 0,  0,  1],
        ]),
]

RotMatrix = typing.Tuple[typing.Tuple[int, int, int], typing.Tuple[int, int, int], typing.Tuple[int, int, int]]

idRotDict: typing.Dict[int, RotMatrix] = {}
rotIdDict: typing.Dict[RotMatrix, int] = {}

cur = numpy.identity(3, int)

for xrot in range(4):
    for yrot in range(4):
        for zrot in range(4):
            curtuple: RotMatrix = totuple(cur) # type: ignore
            if curtuple not in rotIdDict:
                rotId = len(rotIdDict)
                idRotDict[rotId] = curtuple
                rotIdDict[curtuple] = rotId
            cur = numpy.matmul(cur, baseRotations[2])
        cur = numpy.matmul(cur, baseRotations[1])
    cur = numpy.matmul(cur, baseRotations[0])

def addData(a, b) -> typing.List[int]: # type: ignore

    newCoord = numpy.matmul(numpy.linalg.inv(idRotDict[a[3]]), numpy.array([b[0], b[1], b[2]])) + numpy.array([a[0], a[1], a[2]])
    newRotId = rotIdDict[totuple(numpy.matmul(idRotDict[b[3]], idRotDict[a[3]]))] # type: ignore

    return [newCoord[0], newCoord[1], newCoord[2], newRotId]

def addcoord(a: Coord, b: Coord) -> Coord:
    return [a[0] + b[0], a[1] + b[1], a[2] + b[2]]

def subcoord(a: Coord, b: Coord) -> Coord:
    return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]

def tryMerge(scan1: ScannerData, scan2: ScannerData) -> list:
    # no need to rotate, rotate is done from the caller side
    # callee side: only check translations
    counts: typing.Dict[typing.Tuple[int, int, int], int] = {}
    for d1 in scan1:
        for d2 in scan2:
            diff: typing.Tuple[int, int, int] = tuple(subcoord(d1, d2)) # type: ignore
            counts.setdefault(diff, 0)
            counts[diff] += 1
            if counts[diff] >= 12:
                print('merge success')
                return [True, *diff]
    return [False, 0, 0, 0]

known = [True, *[False for i in range(len(data) - 1)]]
mergeData: typing.List[typing.List[int]] = [[0, 0, 0, 0] for i in range(len(data))]
allBeacon = set(data[0])
rotationData: typing.List[typing.List[ScannerData]] = [[[totuple(numpy.matmul(rot, pos)) for pos in dat] for rot in rotIdDict] for dat in data] # type: ignore

def dfs(cur):
    for rotid, datcur in enumerate(rotationData[cur]):
        for i in range(len(data)):
            if not known[i]:
                success, *result = tryMerge(datcur, data[i])
                if success:
                    known[i] = True
                    undorel = numpy.matmul(numpy.linalg.inv(idRotDict[rotid]), result)
                    result = [undorel[0], undorel[1], undorel[2], rotid]
                    mergeData[i] = addData(mergeData[cur], result)
                    print(i)
                    print(mergeData[cur])
                    print(result)
                    print(mergeData[i])
                    print(mergeData)
                    datai = [numpy.array(mergeData[i][0:3]) + numpy.matmul(numpy.linalg.inv(idRotDict[mergeData[i][3]]), pos) for pos in data[i]]
                    for j in datai:
                        allBeacon.add(totuple(j)) # type: ignore
                    dfs(i)

dfs(0)

print(known)
print(mergeData)
print(len(allBeacon))
