#!/usr/bin/env python3

count = 0
with open("input.txt") as infile:
    prev3 = int(infile.readline())
    prev2 = int(infile.readline())
    prev = int(infile.readline())
    current = infile.readline()
    while current != "":
        if int(current) + prev + prev2 > prev + prev2 + prev3:
            count += 1
        prev3 = prev2
        prev2 = prev
        prev = int(current)
        current = infile.readline()
print(count)


