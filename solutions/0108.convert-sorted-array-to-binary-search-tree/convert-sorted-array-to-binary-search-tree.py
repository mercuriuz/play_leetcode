# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.createBST(nums, 0, len(nums) - 1)    
    
    def createBST(self, arr, begin, end):
        if begin > end:
            return None
        middle = (begin + end) // 2
        node = TreeNode(arr[middle])
        node.left = self.createBST(arr, begin, middle - 1)
        node.right = self.createBST(arr, middle + 1, end)
        return node