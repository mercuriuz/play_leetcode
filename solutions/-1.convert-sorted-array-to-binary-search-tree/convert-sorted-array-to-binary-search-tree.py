# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        half = len(nums) // 2
        t = TreeNode(nums[half])
        t.left = self.sortedArrayToBST(nums[:half])
        t.right = self.sortedArrayToBST(nums[half+1:])
        return t