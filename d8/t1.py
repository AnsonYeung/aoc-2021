#!/usr/bin/env python3
import sys
data = sys.stdin.read().split('\n')[:-1]

display = [x.split(" | ")[1].split(" ") for x in data]

lens = [len(x) for y in display for x in y]
print(sum(lens.count(x) for x in [2, 3, 4, 7]))
