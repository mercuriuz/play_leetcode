class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        match_dict = dict()
        size = len(nums)
        result = []
        if size < 2:         
            return result
        for idx in range(size):
            if match_dict.get(target - nums[idx]) is not None:
                result = [idx, match_dict.get(target-nums[idx])]
                break
            match_dict[nums[idx]] = idx
        return result

