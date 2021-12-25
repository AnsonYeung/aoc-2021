#!/usr/bin/env python3
import sys
data = sys.stdin.read().split('\n')[:-1]

adjList = {}

for line in data:
    nodes = line.split('-')
    adjList[nodes[0]] = adjList.get(nodes[0], [])
    adjList[nodes[0]].append(nodes[1])
    adjList[nodes[1]] = adjList.get(nodes[1], [])
    adjList[nodes[1]].append(nodes[0])

visited = []
def dfs(cur, extra):
    if cur == 'end': return 1
    if cur in visited and not extra: return 0
    if cur == 'start' and len(visited) != 0: return 0
    isExtra = False
    if cur in visited:
        extra = False
        isExtra = True
    elif 'a' <= cur[0] <= 'z':
        visited.append(cur)
    total = 0
    for n in adjList[cur]:
        total += dfs(n, extra)
    if cur in visited and not isExtra:
        visited.remove(cur)
    return total

print(dfs('start', True))
print(visited)


