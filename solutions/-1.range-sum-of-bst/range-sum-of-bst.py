# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        sum = 0
        if root is not None:
            if root.val >= L and root.val <= R:
                sum += root.val
            sum += self.rangeSumBST(root.left, L, R)
            sum += self.rangeSumBST(root.right, L, R)
        return sum