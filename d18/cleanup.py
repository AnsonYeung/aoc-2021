#!/usr/bin/env python3
import sys
data = sys.stdin.read().split('\n')[:-1]

class SnailfishTreeNode:

    def __init__(self, parent, isLeft: 'bool', left, right) -> None:
        self.parent: SnailfishTreeNode = parent
        if self.parent is not None:
            if isLeft: self.parent.left = self
            else: self.parent.right = self
        self.isLeft: bool = isLeft
        self.left: SnailfishTreeNode = left
        if self.left is not None:
            self.left.isLeft = True
            self.left.parent = self
        self.right: SnailfishTreeNode = right
        if self.right is not None:
            self.right.isLeft = False
            self.right.parent = self

    def __str__(self) -> str:
        return f'[{self.left},{self.right}]'

class SnailfishValueNode(SnailfishTreeNode):

    def __init__(self, value: int, parent: SnailfishTreeNode, isLeft: bool) -> None:
        self.parent: SnailfishTreeNode = parent
        if self.parent is not None:
            if isLeft: self.parent.left = self
            else: self.parent.right = self
        self.value: int = value
        self.isLeft: bool = isLeft

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
        while not isinstance(cur, SnailfishValueNode):
            cur = cur.right
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
        while not isinstance(cur, SnailfishValueNode):
            cur = cur.left
        return cur

    def __str__(self):
        return str(self.value)

#class SnailfishRootNode(SnailfishTreeNode):
#
#    def __init__(self, left, right) -> None:
#        super().__init__(None, False, left, right)

def findExplode(root: SnailfishTreeNode, level = 4) -> 'tuple[SnailfishTreeNode, bool]':
    if isinstance(root, SnailfishValueNode): return root, False
    if level <= 0 and isinstance(root.left, SnailfishValueNode) and isinstance(root.right, SnailfishValueNode):
        l = root.left.getLeft()
        if l is not None:
            l.value += root.left.value
        r = root.right.getRight()
        if r is not None:
            r.value += root.right.value
        newNode = SnailfishValueNode(0, root.parent, root.isLeft)
        return newNode, True
    status = False
    root.left, status = findExplode(root.left, level - 1)
    if status: return root, status
    root.right, status = findExplode(root.right, level - 1)
    return root, status

def find10(root: SnailfishTreeNode) -> 'tuple[SnailfishTreeNode, bool]':
    if isinstance(root, SnailfishValueNode) and root.value >= 10:
        newNode = SnailfishTreeNode(root.parent, root.isLeft, None, None)
        # Constructing value node will automatically link to parent
        SnailfishValueNode(root.value // 2, newNode, True)
        SnailfishValueNode(root.value - root.value // 2, newNode, False)
        return newNode, True
    if isinstance(root, SnailfishValueNode): return root, False
    status: bool = False
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

def mag(root: SnailfishTreeNode) -> int:
    if isinstance(root, SnailfishValueNode):
        return root.value
    return 3 * mag(root.left) + 2 * mag(root.right)

def parse(l, p: 'None|SnailfishTreeNode', isLeft: bool) -> SnailfishTreeNode:
    if isinstance(l, int):
        assert p is not None
        return SnailfishValueNode(l, p, isLeft)
    cur = SnailfishTreeNode(p, isLeft, None, None)
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
        res = SnailfishTreeNode(None, False, res, r)
        res = reduce(res)

assert res;
print(res)
print(mag(res))

maxmag = 0
for i in range(len(snailfishNumbers)):
    for j in range(i + 1, len(snailfishNumbers)):
        s = SnailfishTreeNode(None, False, parse(snailfishNumbers[i], None, False), parse(snailfishNumbers[j], None, False))
        s = reduce(s)
        if mag(s) > maxmag:
            maxmag = mag(s)
        s = SnailfishTreeNode(None, False, parse(snailfishNumbers[j], None, False), parse(snailfishNumbers[i], None, False))
        s = reduce(s)
        if mag(s) > maxmag:
            maxmag = mag(s)

print(maxmag)
