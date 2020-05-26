# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root or (not root.left and not root.right):
            return
        self.flatten(root.left)
        self.flatten(root.right)
        if not root.left:
            return
        else:
            tmp = root.right
            root.right = root.left
            root.left = None
            right = root.right
            while right.right:
                right = right.right
            right.right = tmp
            return