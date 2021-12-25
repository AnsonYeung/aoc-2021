#!/usr/bin/env python3
import sys
import heapq
data = sys.stdin.read().split('\n')[:-1]
data = [[int(x) for x in row] for row in data]
#print(len(data))
#print(len(data[0]))
times = 5
M = 100
N = M * times
data = [[(data[m][n] + i + j - 1) % 9 + 1 for j in range(times) for n in range(M)] for i in range(times) for m in range(M)]
#ndata = []
#for i in range(N):
#    ndata.append([])
#    for j in range(N):
#        ndata[i].append((data[i % M][j % M] + i // M + j // M - 1) % 9 + 1)
#data = ndata
#print(len(data))
#print(len(data[0]))
minheap: 'list[tuple[int, int, int]]' = [(0, 0, 0)]
heapq.heapify(minheap)
risk = [[1000000 for __ in range(N)] for _ in range(N)]
done = [[False for __ in range(N)] for _ in range(N)]

while len(minheap) > 0:
    cur = heapq.heappop(minheap)
    if done[cur[1]][cur[2]]:
        continue
    risk[cur[1]][cur[2]] = cur[0]
    if cur[1] == N-1 and cur[2] == N-1: break
    done[cur[1]][cur[2]] = True
    def addtoheap(x, y, c):
        if 0 <= x < N and 0 <= y < N:
            if c + data[x][y] < risk[x][y]:
                risk[x][y] = c + data[x][y]
                heapq.heappush(minheap, (c + data[x][y], x, y))
    addtoheap(cur[1] - 1, cur[2], cur[0])
    addtoheap(cur[1] + 1, cur[2], cur[0])
    addtoheap(cur[1], cur[2] - 1, cur[0])
    addtoheap(cur[1], cur[2] + 1, cur[0])
    # print(cur[1], cur[2], risk[cur[1]][cur[2]])

print(risk[N - 1][N - 1])
