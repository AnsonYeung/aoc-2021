#!/usr/bin/env python3
import sys
data = sys.stdin.read().split('\n')[:-1]

err = []
pts = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
        }
for d in data:
    st = []
    for c in d:
        if c == "(":
            st.append(")")
        elif c == "[":
            st.append("]")
        elif c == "<":
            st.append(">")
        elif c == "{":
            st.append("}")
        else:
            if c != st.pop():
                break
    else:
        if len(st) != 0:
            sc = 0
            while len(st) > 0:
                sc = sc * 5 + pts[st.pop()]
            err.append(sc)
            print(sc)
print(err)

err = sorted(err)
print(len(err))
print(err[len(err)//2])
