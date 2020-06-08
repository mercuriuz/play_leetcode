# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        n = len(lists)
        if n == 0:
            return
        def merge(lists, start, end):
            if start >= end:
                return lists[start]
            mid = (start+end) // 2
            l1 = merge(lists, start, mid)
            l2 = merge(lists, mid+1, end)
            return self.mergeLists(l1, l2)
        return merge(lists, 0, n-1)


    def mergeLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        dummy0 = dummy1 = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                dummy1.next = l1
                l1 = l1.next
            else:
                dummy1.next = l2
                l2 = l2.next
            dummy1 = dummy1.next
        if l1:
            dummy1.next = l1
        if l2:
            dummy1.next = l2
        return dummy0.next