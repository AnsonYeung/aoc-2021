#!/usr/bin/env python3
import sys
from collections import deque
data = sys.stdin.read().split('\n')[:-1]

totalVersion = 0

def parse_packet(data: 'str') -> 'tuple[int, int]':
    global totalVersion
    # if all(bit == '0' for bit in data): return len(data)
    version = int(data[0:3], 2)
    totalVersion += version
    pack_type = int(data[3:6], 2)
    if pack_type == 4:
        # literal value
        cur = 6
        value = 0
        while data[cur] == '1':
            value = value * 16 + int(data[cur+1:cur+5], 2)
            cur += 5
        value = value * 16 + int(data[cur+1:cur+5], 2)
        cur += 5
        return (cur, value)

    # operator packet
    lengthType = int(data[6], 2)
    subpacket = []
    totallength = 0
    if lengthType == 0:
        l = int(data[7:7+15], 2)
        cur = 7+15
        d = data[cur:]
        while cur < l + 7 + 15:
            subl = parse_packet(d)
            subpacket.append(subl[1])
            d = d[subl[0]:]
            cur += subl[0]
        totallength = l + 7 + 15
    else:
        # lengthType 1
        numPack = int(data[7:7+11], 2)
        l = 7 + 11
        cur = l
        d = data[cur:]
        num = 0
        while num < numPack:
            subl = parse_packet(d)
            subpacket.append(subl[1])
            d = d[subl[0]:]
            l += subl[0]
            num += 1
        totallength = l

    print(pack_type, subpacket)
    if pack_type == 0:
        return (totallength, sum(subpacket))
    elif pack_type == 1:
        prod = 1
        for val in subpacket:
            prod *= val
        return (totallength, prod)
    elif pack_type == 2:
        return (totallength, min(subpacket))
    elif pack_type == 3:
        return (totallength, max(subpacket))
    elif pack_type == 5:
        return (totallength, 1 if subpacket[0] > subpacket[1] else 0)
    elif pack_type == 6:
        return (totallength, 1 if subpacket[0] < subpacket[1] else 0)
    elif pack_type == 7:
        return (totallength, 1 if subpacket[0] == subpacket[1] else 0)
    return (totallength, 0)

bits = ""

for hexv in data[0]:
    val = int(hexv, 16)
    for i in [8, 4, 2, 1]:
        bits += '1' if val & i else '0'

# print(bits)
_, value = parse_packet(bits)

print(totalVersion)
print(value)
