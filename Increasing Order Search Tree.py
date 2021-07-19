"""
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now
the root of the tree, and every node has no left child and only one right child.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # Morris in-order traversal
        #         dummy = tail = TreeNode()
        #         while root is not None:
        #             if root.left is not None:
        #                 pred = root.left
        #                 while pred.right is not None:
        #                     pred = pred.right

        #                 pred.right = root
        #                 left = root.left
        #                 root.left = None
        #                 root = left
        #             else:
        #                 tail = tail.right = root
        #                 root = root.right
        #         return dummy.right

        vals = []

        # Easy recursive Inorder Traversal to get our values to insert.
        def inord(node):
            if not node:
                return
            inord(node.left)
            vals.append(node.val)
            inord(node.right)

        inord(root)
        # Create a new tree to return.
        tree = TreeNode(val=vals[0])
        # Use a sentinel so we dont lose our tree location in memory.
        tmp = tree
        # Iterate through our vals, creating a new right node with the current val.
        for i in vals[1:]:
            tmp.right = TreeNode(val=i)
            # Move the sentinel to the next node.
            tmp = tmp.right

        return tree
