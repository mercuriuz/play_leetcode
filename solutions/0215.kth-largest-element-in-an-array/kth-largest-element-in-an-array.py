class Solution:
    def findKthLargest(self, nums, k):
        n = len(nums)
        if (k > n):
            return
        index = self.quickSort(nums, 0, n-1, k)
        return nums[index]
        
        
    def quickSort(self, nums, l, r, k):
        if l >= r:
            return l
        p = self.partition(nums, l, r)
        if p + 1 == k:
            return p
        if p + 1 > k:
            return self.quickSort(nums, l, p -1, k)
        else:
            return self.quickSort(nums, p + 1, r, k)


    def partition(self, nums, l, r):
        v = nums[l]
        j = l
        i = l + 1
        while i <= r:
            if nums[i] >= v:
                nums[j+1],nums[i] = nums[i],nums[j+1]
                j += 1
            i += 1
        nums[l], nums[j] = nums[j], nums[l]
        return j