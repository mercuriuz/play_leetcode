# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head is None:
            return None
        def find(head, tail):
            if head == tail:
                return None
            fast = head
            slow = head
            while fast.next is not tail and fast.next.next is not tail:
                fast = fast.next.next
                slow = slow.next
            t = TreeNode(slow.val)
            t.left = find(head, slow)
            t.right = find(slow.next, tail)
            return t
        return find(head, None)