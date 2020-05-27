class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for idx in range(len(nums)):
            if nums[idx] == nums[idx+1]:
                return nums[idx]