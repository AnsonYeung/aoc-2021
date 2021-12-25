#!/usr/bin/env python3
import sys
data = sys.stdin.read().split('\n')[:-1]

template = data[0]

rules: 'dict[str, str]' = {}
for i in range(2, len(data)):
    l = data[i].split(' -> ')
    rules[l[0]] = l[1]

counts: 'dict[str, int]' = {}
for i in range(1, len(template)):
    counts.setdefault(template[i - 1: i + 1], 0)
    counts[template[i - 1: i + 1]] += 1

for i in range(40):
    newcounts: 'dict[str, int]' = {}
    for s in counts:
        newcounts.setdefault(s[0] + rules[s], 0)
        newcounts[s[0] + rules[s]] += counts[s]
        newcounts.setdefault(rules[s] + s[1], 0)
        newcounts[rules[s] + s[1]] += counts[s]
    counts = newcounts

cnts: 'dict[str, int]' = {}
cnts[template[0]] = 1
cnts[template[-1]] += 1
print(cnts)
for s in counts:
    cnts.setdefault(s[0], 0)
    cnts[s[0]] += counts[s]
    cnts.setdefault(s[1], 0)
    cnts[s[1]] += counts[s]

print(cnts)

print(max(cnts.values()) // 2 - min(cnts.values()) // 2)
