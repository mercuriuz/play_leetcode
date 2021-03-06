class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(1 << len(nums)):
            tmp = []
            for j in range(len(nums)):
                if i & (1 << j):
                    tmp.append(nums[j])
            res.append(tmp)
        return res