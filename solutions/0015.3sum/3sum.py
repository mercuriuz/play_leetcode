class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        tmp_dict = {}
        a = set()
        b = set()
        result = []
        for i in nums:
            if tmp_dict.get(i) is None:
                tmp_dict[i] = 1
            else:
                tmp_dict[i] += 1
        for i in nums:
            tmp_dict[i] -= 1
            for k in a:
                if -(k + i) in tmp_dict and tmp_dict[-(k+i)] > 0:
                    if -(k+i) >= i:
                        b.add((i, k, -(k+i)))
                    elif -(k+i) <= i:
                        b.add((-(k+i), i, k))
                    else:
                        b.add((i, -(k+i), k))
            a.add(i)
        for item in b:
            tmp = list(item)
            tmp.sort()
            result.append(tmp)
        return result

