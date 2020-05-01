class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 0:
            return None
        if size == 1:
            return 0
        if size == 2:
            return 0 if nums[0] >= nums[1] else 1
        for idx in range(size):
            if idx == 0:
                if nums[idx] >= nums[idx+1]:
                    return 0
            if idx == size - 1:
                if nums[idx] >= nums[idx-1]:
                    return size-1
            if nums[idx] >= nums[idx-1] and nums[idx] >= nums[idx+1]:
                return idx