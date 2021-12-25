#!/usr/bin/env python3
hpos = 0
depth = 0
aim = 0
with open("input.txt") as infile:
    cmd = infile.readline()
    while cmd != "":
        parsed = cmd.split(" ")
        if parsed[0] == "forward":
            hpos += int(parsed[1])
            depth += int(parsed[1]) * aim
        elif parsed[0] == "down":
            aim += int(parsed[1])
        elif parsed[0] == "up":
            aim -= int(parsed[1])
        else:
            raise Exception(f"Unknown command {parsed[0]}")
        cmd = infile.readline()

print(hpos)
print(depth)
print(hpos * depth)
