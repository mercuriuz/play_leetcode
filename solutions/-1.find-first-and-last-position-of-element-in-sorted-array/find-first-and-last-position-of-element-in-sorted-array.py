class Solution:
    def _binarySearch(self, nums, start, end, target, result):
        mid = start + (end - start) // 2
        if nums[mid] == target:
            result.append(mid)
        if start < end:
            self._binarySearch(nums, start, mid, target, result)
            self._binarySearch(nums, mid+1, end, target, result)
        else:
            return

    def searchRange(self, nums, target):
        start = 0
        end = len(nums) - 1
        result = []
        if not nums or len(nums) == 0:
            return [-1, -1]

        self._binarySearch(nums, start, end, target, result)
        if len(result) == 0:
            return [-1, -1]
        if len(result) == 1:
            return [result[0], result[0]]
        minimum, maximum = result[0], result[0]
        for num in result:
            if num < minimum:
                minimum = num
            elif num > maximum:
                maximum = num
        return [minimum, maximum]