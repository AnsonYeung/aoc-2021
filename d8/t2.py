#!/usr/bin/env python3
import sys
data = sys.stdin.read().split('\n')[:-1]

display = [x.split(" | ")[1].split(" ") for x in data]
numbers = [x.split(" | ")[0].split(" ") for x in data]

total = 0

for i in range(len(display)):
    digit = ""
    one = list()
    four = list()
    for d in numbers[i]:
        if len(d) == 2:
            one = list(d)
        elif len(d) == 4:
            four = list(d)
    bd = four.copy()
    bd.remove(one[0])
    bd.remove(one[1])
    for d in display[i]:
        if len(d) == 2:
            digit += '1'
        elif len(d) == 3:
            digit += '7'
        elif len(d) == 4:
            digit += '4'
        elif len(d) == 7:
            digit += '8'
        elif len(d) == 5:
            if all(x in d for x in one):
                digit += '3'
            elif all(x in d for x in bd):
                digit += '5'
            else:
                digit += '2'
        else:
            if not all(x in d for x in one):
                digit += '6'
            elif all(x in d for x in bd):
                digit += '9'
            else:
                digit += '0'
    total += int(digit)
print(total)
            

