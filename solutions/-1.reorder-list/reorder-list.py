# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def find_mid(head):
            slow, fast = head, head
            while fast.next is not None:
                slow = slow.next
                fast = fast.next
                if fast.next is not None:
                    fast = fast.next
            return slow
        
        def reverse(head):
            prev = None
            while head is not None:
                next = head.next
                head.next = prev
                prev = head
                head = next
            return prev
        if head is None:
            return
        mid = find_mid(head)
        l2 = mid.next
        mid.next = None
        l2 = reverse(l2)
        tmp = head
        while l2 is not None:
            n1 = tmp.next
            n2 = l2.next
            tmp.next = l2
            l2.next = n1
            tmp = n1
            l2 = n2