#!/usr/bin/env python3
import sys
data = sys.stdin.read().split('\n')[:-1]

err = 0
pts = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
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
                err += pts[c]
                break

print(err)

