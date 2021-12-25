#!/usr/bin/env python3
import sys
data = sys.stdin.read().split('\n')[:-1]
p1 = 7
p2 = 8

board = [[[[0 for __ in range(21)] for _ in range(0, 11)] for ___ in range(21)] for ____ in range(0, 11)]
board[p1][0][p2][0] = 1
p1t = 0
p2t = 0
quantumDice = [1, 2, 3]
threeDice = [0]
for _ in range(3):
    nDice = []
    for x in threeDice:
        for y in quantumDice:
            nDice.append(x + y)
    threeDice = nDice

def rsum(a) -> int:
    try:
        return sum(a)
    except:
        return sum(rsum(i) for i in a)
print(threeDice)

while rsum(board) > 0:
    # p1 turn
    nboard = [[[[0 for __ in range(21)] for _ in range(0, 11)] for ___ in range(21)] for ____ in range(0, 11)]
    for p1p in range(1, 11):
        for p1s in range(21):
            for diceResult in threeDice:
                newp = (diceResult + p1p - 1) % 10 + 1
                news = p1s + newp
                if news >= 21:
                    p1t += rsum(board[p1p][p1s])
                else:
                    for _ in range(21):
                        for __ in range(0, 11):
                            nboard[newp][news][__][_] += board[p1p][p1s][__][_]
    board = nboard
    print(p1t)
    nboard = [[[[0 for __ in range(21)] for _ in range(0, 11)] for ___ in range(21)] for ____ in range(0, 11)]
    # p2 turn
    for p2p in range(1, 11):
        for p2s in range(21):
            for diceResult in threeDice:
                newp = (diceResult + p2p - 1) % 10 + 1
                news = p2s + newp
                if news >= 21:
                    p2t += sum(sum(p1[p2p][p2s] for p1 in x) for x in board)
                else:
                    for _ in range(21):
                        for __ in range(0, 11):
                            nboard[__][_][newp][news] += board[__][_][p2p][p2s]
    board = nboard
    print(p2t)

print(p1t)
print(p2t)
    

