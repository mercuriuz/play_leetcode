# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = l1
        cn = 0
        while l1 and l2:
            res = cn + (l1.val) + (l2.val)
            cn, val = res // 10, res % 10
            l1.val = val
            prev, l1, l2 = l1, l1.next, l2.next
        l = l1 or l2
        prev.next = l
        while l and cn:
            res = cn + l.val
            cn, val = res // 10, res % 10
            l.val = val
            prev, l = l, l.next
        if cn:
            prev.next = ListNode(cn)
        return dummy.next