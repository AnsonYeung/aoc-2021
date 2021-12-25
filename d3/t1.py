#!/usr/bin/env python3
with open("input.txt") as infile:
    i = infile.read().split('\n')[:-1]

print(len(i))       

print(len(i[0]))

a = [0] * 12
b = [0] * 12
for x in i:
    for y, c in enumerate(x):
        if c == '1':
            a[y] += 1
        else:
            b[y] += 1

res = ''
res2 = ''
print(a)
print(b)
for j in range(len(a)):
    if a[j] > b[j]:
        print('1', end='')
        res += '1'
        res2 += '0'
    else:
        print('0', end='')
        res += '0'
        res2 += '1'

print()
print(res)
print(int(res, 2))
print(int(res, 2) * int(res2, 2))


