class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        import sys
        first, second =  sys.maxsize, sys.maxsize
        for num in nums:
            if num > second:
                return True
            if num <= first:
                first = num
            else:
                second = num
        return False
            