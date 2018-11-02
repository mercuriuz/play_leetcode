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
        p = dummy
        cn = 0
        while l1 or l2:
            res = cn + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            cn = res // 10
            val = res % 10
            p.next = ListNode(val)
            p = p.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        if cn != 0:
            p.next = ListNode(cn)
        res = dummy.next
        result = []
        while res:
            result.append(res.val)
            res = res.next
        return result