#!/usr/bin/env python3
import sys
import copy
data = sys.stdin.read().split('\n')[:-1]

class SnailfishTreeNode:

    def __init__(self, parent, value = -1, isLeft = False, left = None, right = None):
        self.parent: SnailfishTreeNode = parent
        if self.parent is not None:
            if isLeft: self.parent.left = self
            else: self.parent.right = self
        self.value: int = value
        self.isLeft: bool = isLeft
        self.left: 'None|SnailfishTreeNode' = left
        if self.left is not None:
            self.left.isLeft = True
            self.left.parent = self
        self.right: 'None|SnailfishTreeNode' = right
        if self.right is not None:
            self.right.isLeft = False
            self.right.parent = self

    def __str__(self) -> str:
        l = self.left
        if l is not None and l.value != -1:
            l = l.value
        r = self.right
        if r is not None and r.value != -1:
            r = r.value
        return '['+str(l)+','+str(r)+']'

    def getLeft(self):
        cur = self
        while cur.isLeft:
            cur = cur.parent
            if cur is None:
                return None
        cur = cur.parent
        if cur is None:
            return None
        cur = cur.left
        tmp = cur.right
        while tmp is not None:
            cur = tmp
            tmp = cur.right
        return cur

    def getRight(self):
        cur = self
        while not cur.isLeft:
            cur = cur.parent
            if cur is None:
                return None
        cur = cur.parent
        if cur is None:
            return None
        cur = cur.right
        tmp = cur.left
        while tmp is not None:
            cur = tmp
            tmp = cur.left
        if cur.value != -1:
            return cur
        else:
            return None

def findExplode(root, level=4):
    if root.value != -1: return root, False
    if level <= 0 and root.left.value != -1 and root.right.value != -1:
        l = root.left.getLeft()
        if l is not None:
            l.value += root.left.value
        r = root.right.getRight()
        if r is not None:
            r.value += root.right.value
        newNode = SnailfishTreeNode(root.parent, 0, root.isLeft)
        return newNode, True
    status = False
    root.left, status = findExplode(root.left, level - 1)
    if status: return root, status
    root.right, status = findExplode(root.right, level - 1)
    return root, status

def find10(root):
    if root.value >= 10:
        newNode = SnailfishTreeNode(root.parent, -1, root.isLeft)
        newNodeLeft = SnailfishTreeNode(newNode, root.value // 2, True)
        newNodeRight = SnailfishTreeNode(newNode, root.value - root.value // 2, False)
        return newNode, True
    if root.value != -1: return root, False
    status = False
    root.left, status = find10(root.left)
    if status: return root, status
    root.right, status = find10(root.right)
    return root, status

def reduce(root: SnailfishTreeNode) -> SnailfishTreeNode:
    reduced = True
    while reduced:
        reduced = False
        root, reduced = findExplode(root)
        if reduced: continue
        root, reduced = find10(root)
    return root

def mag(root) -> int:
    if root.value != -1:
        return root.value
    return 3 * mag(root.left) + 2 * mag(root.right)

def parse(l, p: 'None|SnailfishTreeNode', isLeft: bool) -> SnailfishTreeNode:
    if isinstance(l, int):
        return SnailfishTreeNode(p, l, isLeft)
    cur = SnailfishTreeNode(p, -1, isLeft)
    cur.left = parse(l[0], cur, True)
    cur.right = parse(l[1], cur, False)
    return cur

snailfishNumbers = []
for l in data:
    snailfishNumbers.append(eval(l))


res = None
for num in snailfishNumbers:
    r = parse(num, None, False)
    if res is None:
        res = r
        res = reduce(res)
    else:
        res = SnailfishTreeNode(None, -1, False, res, r)
        res = reduce(res)

assert res;
print(res)
print(mag(res))

maxmag = 0
for i in range(len(snailfishNumbers)):
    for j in range(i + 1, len(snailfishNumbers)):
        s = SnailfishTreeNode(None, -1, False, parse(snailfishNumbers[i], None, False), parse(snailfishNumbers[j], None, False))
        s = reduce(s)
        if mag(s) > maxmag:
            maxmag = mag(s)
        s = SnailfishTreeNode(None, -1, False, parse(snailfishNumbers[j], None, False), parse(snailfishNumbers[i], None, False))
        s = reduce(s)
        if mag(s) > maxmag:
            maxmag = mag(s)

print(maxmag)
