# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        level = []
        if root is None:
            return level
        
        from collections import deque
        queue = deque([root,])
        depth = 0
        while queue:
            level.append([])
            level_len = len(queue)
            for _ in range(level_len):
                tmp = queue.popleft()
                level[depth].append(tmp.val)
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
            depth += 1
        return level