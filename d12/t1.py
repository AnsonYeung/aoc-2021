#!/usr/bin/env python3
import sys
data = sys.stdin.read().split('\n')[:-1]

adjList = {}

for line in data:
    nodes = line.split('-')
    if nodes[0] not in adjList:
        adjList[nodes[0]] = [nodes[1]]
    else:
        adjList[nodes[0]].append(nodes[1])
    if nodes[1] not in adjList:
        adjList[nodes[1]] = [nodes[0]]
    else:
        adjList[nodes[1]].append(nodes[0])

visited = []
def dfs(cur):
    if cur == 'end': return 1
    if cur in visited: return 0
    if 'a' <= cur[0] <= 'z':
        visited.append(cur)
    total = 0
    for n in adjList[cur]:
        total += dfs(n)
    if cur in visited:
        visited.remove(cur)
    return total

print(dfs('start'))

