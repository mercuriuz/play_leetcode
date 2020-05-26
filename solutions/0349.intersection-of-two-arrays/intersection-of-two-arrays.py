class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num in nums2:
            if num not in res:
                if num in nums1:
                    res.append(num)
        return res