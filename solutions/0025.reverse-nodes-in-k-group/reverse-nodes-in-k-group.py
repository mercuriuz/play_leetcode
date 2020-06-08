# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        if k <= 1 or not head:
            return head
        for _ in range(k-1):
            if not head.next:
                return dummy.next
            head = head.next
        next_head = head.next
        head.next = None
        last = dummy.next
        new_head = self.reverse(dummy.next)
        last.next = self.reverseKGroup(next_head, k)

        return new_head

    def reverse(self, head):
        new_head = None
        while head:
            node = head
            head = head.next

            node.next = new_head
            new_head = node
        return new_head