# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        queue = collections.deque()
        queue.append([root, root.val])
        while queue:
            current_node = queue.popleft()
            node, value = current_node
            # if not (node.left or node.right) and value == sum:
            if not node.left and not node.right and value == sum:
                return True
            if node.left:
                queue.append([node.left, value + node.left.val])
            if node.right:
                queue.append([node.right, value + node.right.val])
        return False