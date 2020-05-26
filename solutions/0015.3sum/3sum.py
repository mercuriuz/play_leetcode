class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        num_dict = {}
        for i in nums:
            num_dict[i] = num_dict.get(i, 0) + 1
        if 0 in num_dict and num_dict[0] > 2:
            res = [[0,0,0]]
        else:
            res = []
        neg = sorted(filter(lambda x: x < 0, num_dict))
        pos = sorted(filter(lambda x: x >= 0, num_dict))
        for i in neg:
            for j in pos:
                if -(i+j) in num_dict:
                    if -(i+j) in (i, j) and num_dict[-(i+j)]>1:
                        res.append([i,j,-(i+j)])
                    elif -(i+j) < i or -(i+j) > j:
                        res.append([i,-(i+j), j])
        return res
