class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cnt = {}
        for num in nums:
            cnt[num] = cnt.get(num, 0) + 1
        max_frequency = 0
        freq = {}
        for key in cnt.keys():
            count = cnt[key]
            max_frequency = count if count > max_frequency else max_frequency
            freq[count] = freq.get(count, []) + [key]
        total = 0
        result = []
        for idx in range(max_frequency, 0, -1):
            if total >= k:
                break
            elif freq.get(idx):
                result += freq[idx]
                total += len(freq[idx])
        return result