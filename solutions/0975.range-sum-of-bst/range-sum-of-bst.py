# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.res = 0
        self.dfs(root, L, R)
        return self.res
    def dfs(self, root, l, r):
        if not root:
            return
        if l <= root.val <= r:
            self.res += root.val
            self.dfs(root.left, l, r)
            self.dfs(root.right, l, r)
        if root.val < l:
            self.dfs(root.right, l, r)
        if root.val > r:
            self.dfs(root.left, l, r)