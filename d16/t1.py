#!/usr/bin/env python3
import sys
from collections import deque
data = sys.stdin.read().split('\n')[:-1]

totalVersion = 0

def parse_packet(data: 'str') -> int:
    global totalVersion
    if all(bit == '0' for bit in data): return len(data)
    version = int(data[0:3], 2)
    totalVersion += version
    pack_type = int(data[3:6], 2)
    if pack_type == 4:
        # literal value
        cur = 6
        while data[cur] == '1':
            cur += 5
        cur += 5
        return cur

    # operator packet
    lengthType = int(data[6], 2)
    if lengthType == 0:
        l = int(data[7:7+15], 2)
        cur = 7+15
        d = data[cur:]
        while cur < l + 7 + 15:
            subl = parse_packet(d)
            d = d[subl:]
            cur += subl
        return l + 7 + 15
    
    # lengthType 1
    numPack = int(data[7:7+11], 2)
    l = 7 + 11
    cur = l
    d = data[cur:]
    num = 0
    while num < numPack:
        subl = parse_packet(d)
        d = d[subl:]
        l += subl
        num += 1

    return l

bits = ""

for hexv in data[0]:
    val = int(hexv, 16)
    for i in [8, 4, 2, 1]:
        bits += '1' if val & i else '0'

# print(bits)
while len(bits) > 0:
    bits = bits[parse_packet(bits):]

print(totalVersion)
