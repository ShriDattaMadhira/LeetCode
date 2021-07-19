"""
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes
with a value in the inclusive range [low, high].
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root is None:
            return 0
        elif low > root.val:
            # print("Root Value:", root.val)
            return self.rangeSumBST(root.right, low, high)
        elif high < root.val:
            # print("Root Value:", root.val)
            return self.rangeSumBST(root.left, low, high)
        else:
            # print("Root Value:", root.val)
            return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
