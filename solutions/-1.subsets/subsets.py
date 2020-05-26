class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sz = len(nums)
        if sz <= 1:
            return [[], nums]
        num = nums[-1]
        tmp = self.subsets(nums[0:sz-1])
        return tmp + [item + [num] for item in tmp]
