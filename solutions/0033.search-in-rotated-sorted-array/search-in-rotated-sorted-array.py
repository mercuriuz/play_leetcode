class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return - 1
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[-1]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1