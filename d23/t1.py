#!/usr/bin/env python3
import sys
# data = sys.stdin.read().split('\n')[:-1]

data = [[1000, 10], [1, 100], [100, 10], [1000, 1]]
target = [[1, 1], [10, 10], [100, 100], [1000, 1000]]

buf = [0 for _ in range(11)]
# bufok = [0, 1, 3, 5, 7, 9, 10]
bufok = [True, True, False, True, False, True, False, True, False, True, True]

minDist = 15000

def dfs(curDist=0):
    global minDist, data, buf
    if curDist > minDist: return
    done = True
    for i in range(4):
        for j in range(2):
            if data[i][j] != target[i][j]:
                done = False
                break
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
                if data[dest][0] == 0:
                    if data[dest][1] == 0:
                        buf[i] = 0
                        data[dest][1] = curval
                        dfs(curDist + curval * (2 + abs(dest * 2 + 2 - i)))
                        data[dest][1] = 0
                        buf[i] = curval
                    elif data[dest][1] == curval:
                        buf[i] = 0
                        data[dest][0] = curval
                        dfs(curDist + curval * (1 + abs(dest * 2 + 2 - i)))
                        data[dest][0] = 0
                        buf[i] = curval

    # move data to buf
    for i in range(4):
        goodval = 1 if i == 0 else 10 if i == 1 else 100 if i == 2 else 1000
        if data[i][0] != 0 and not (data[i][0] == goodval and data[i][1] == goodval):
            curval = data[i][0]
            data[i][0] = 0
            curcoord = i * 2 + 2
            moved = 1
            while curcoord >= 0 and buf[curcoord] == 0:
                if bufok[curcoord]:
                    buf[curcoord] = curval
                    dfs(curDist + curval * moved)
                    buf[curcoord] = 0
                curcoord -= 1
                moved += 1
            curcoord = i * 2 + 2
            moved = 1
            while curcoord < 11 and buf[curcoord] == 0:
                if bufok[curcoord]:
                    buf[curcoord] = curval
                    dfs(curDist + curval * moved)
                    buf[curcoord] = 0
                curcoord += 1
                moved += 1
            data[i][0] = curval
        elif data[i][1] != 0 and data[i][1] != goodval:
            curval = data[i][1]
            data[i][1] = 0
            curcoord = i * 2 + 2
            moved = 2
            while curcoord >= 0 and buf[curcoord] == 0:
                if bufok[curcoord]:
                    buf[curcoord] = curval
                    dfs(curDist + curval * moved)
                    buf[curcoord] = 0
                curcoord -= 1
                moved += 1
            curcoord = i * 2 + 2
            moved = 2
            while curcoord < 11 and buf[curcoord] == 0:
                if bufok[curcoord]:
                    buf[curcoord] = curval
                    dfs(curDist + curval * moved)
                    buf[curcoord] = 0
                curcoord += 1
                moved += 1
            data[i][1] = curval

dfs()
print(minDist)
