#!/usr/bin/env python3
import sys
data = sys.stdin.read().split('\n')[:-1]

order = data[0].split(',')
order = [int(i) for i in order]

max_board_num = 26
max_board = 0

for i in range(2, len(data) - 1, 6):
    board = []
    taken = []
    for j in range(5):
        board.append([int(x) for x in data[i + j].split(' ') if x != ''])
        taken.append([False] * 5)
    print(board)
    for j, num in enumerate(order):
        for x, a in enumerate(board):
            for y, b in enumerate(a):
                if b == num:
                    taken[x][y] = True
                    ok1 = True
                    ok2 = True
                    for n in range(5):
                        ok1 &= taken[n][y]
                        ok2 &= taken[x][n]
                    if ok1 or ok2:
                        # board win
                        if j + 1 < max_board_num:
                            max_board_num = j + 1
                            max_board = num * sum(board[h][k] for h in range(5) for k in range(5) if not taken[h][k])

print(max_board)
print(max_board_num)

