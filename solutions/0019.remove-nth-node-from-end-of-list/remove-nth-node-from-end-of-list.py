# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        walker, runner = head, head
        for _ in range(n):
            walker = walker.next
        if walker is None:
            return runner.next
        while walker.next is not None:
            walker = walker.next
            runner = runner.next
        runner.next = runner.next.next
        return dummy.next