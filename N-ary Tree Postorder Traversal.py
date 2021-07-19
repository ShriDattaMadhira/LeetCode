"""
Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal.
Each group of children is separated by the null value (See examples)
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def result(self, root, res):
        if root:
            for child in root.children:
                self.result(child, res)
            res.append(root.val)
        return res

    def postorder(self, root: 'Node') -> List[int]:
        res = []
        return self.result(root, res)
