#!/usr/bin/env python3


count = 0
with open("input.txt") as infile:
    prev = int(infile.readline())
    current = infile.readline()
    while current != "":
        if int(current) > prev:
            count += 1
        prev = int(current)
        current = infile.readline()
print(count)


