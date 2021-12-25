#!/usr/bin/env python3
import sys
data = sys.stdin.read().split('\n')[:-1]
p1 = 7
p2 = 8

p1s = 0
p2s = 0
nextDice = 1
totalThrow = 0
def throw():
    global nextDice, totalThrow
    nextDice = nextDice % 100 + 1
    totalThrow += 1

while p1s < 1000 and p2s < 1000:
    throws = 0
    while throws < 3:
        p1 += nextDice
        throw()
        throws += 1
    p1 = (p1 - 1) % 10 + 1
    p1s += p1
    if p1s >= 1000: break
    throws = 0
    while throws < 3:
        p2 += nextDice
        throw()
        throws += 1
    p2 = (p2 - 1) % 10 + 1
    p2s += p2

print(totalThrow, p1s, p2s)
print(totalThrow * p1s, totalThrow * p2s)
    

