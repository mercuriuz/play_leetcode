class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        import sys
        first, second =  sys.maxsize, sys.maxsize
        for num in nums:
            if first >= num:
                first = num
            elif first < num and second >= num:
                second = num
            else:
                return True
        return False
            