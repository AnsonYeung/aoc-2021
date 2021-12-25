#!/usr/bin/env python3
import sys
# data = sys.stdin.read().split('\n')[:-1]

# data for part 2
data = [[1000, 1000, 1000, 10], [1, 100, 10, 100], [100, 10, 1, 10], [1000, 1, 100, 1]]
# data for part 1
#data = [[1000, 10], [1, 100], [100, 10], [1000, 1]]
#target = [[1, 1], [10, 10], [100, 100], [1000, 1000]]
# example for part 1
#data = [[10, 1], [100, 1000], [10, 100], [1000, 1]]
# example for part 2
#data = [[10, 1000, 1000, 1], [100, 100, 10, 1000], [10, 10, 1, 100], [1000, 1, 100, 1]]
target = [[1, 1, 1, 1], [10, 10, 10, 10], [100, 100, 100, 100], [1000, 1000, 1000, 1000]]
depth = 4
#depth = 2

buf = [0 for _ in range(11)]
# bufok = [0, 1, 3, 5, 7, 9, 10]
bufok = [True, True, False, True, False, True, False, True, False, True, True]

minDist = 50000

def dfs(curDist=0):
    global minDist, data, buf
    if curDist >= minDist: return
    done = True
    for i in range(4):
        for j in range(depth):
            if data[i][j] != target[i][j]:
                done = False
    if done:
        minDist = curDist
        print(minDist)
        return

    # either move data to buf or buf to data

    # move buf to data
    for i in range(11):
        if buf[i] != 0:
            curval = buf[i]
            dest = 0 if buf[i] == 1 else 1 if buf[i] == 10 else 2 if buf[i] == 100 else 3
            buf[i] = 0
            bufgood = all(buf[j] == 0 for j in range(min(i, dest * 2 + 2), max(i, dest * 2 + 2) + 1))
            buf[i] = curval
            if bufgood:
                if all(data[dest][j] == 0 or data[dest][j] == curval for j in range(depth)):
                    cell = depth - 1
                    while data[dest][cell] != 0: cell -= 1

                    buf[i] = 0
                    data[dest][cell] = curval
                    dfs(curDist + curval * (1 + cell + abs(dest * 2 + 2 - i)))
                    data[dest][cell] = 0
                    buf[i] = curval

    # move data to buf
    for i in range(4):
        goodval = target[i][0]
        # if all good, don't move anything
        if all(data[i][j] == 0 or data[i][j] == goodval for j in range(depth)): continue
        # else, move top
        top = 0
        while data[i][top] == 0: top += 1
        curval = data[i][top]
        data[i][top] = 0
        curcoord = i * 2 + 2
        moved = 1 + top
        while curcoord >= 0 and buf[curcoord] == 0:
            if bufok[curcoord]:
                buf[curcoord] = curval
                dfs(curDist + curval * moved)
                buf[curcoord] = 0
            curcoord -= 1
            moved += 1
        curcoord = i * 2 + 2
        moved = 1 + top
        while curcoord < 11 and buf[curcoord] == 0:
            if bufok[curcoord]:
                buf[curcoord] = curval
                dfs(curDist + curval * moved)
                buf[curcoord] = 0
            curcoord += 1
            moved += 1
        data[i][top] = curval

dfs()
print(minDist)
