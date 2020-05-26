class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            m, n, nums1, nums2 = n, m, nums2, nums1
        if n == 0:
            raise ValueError

        if m == 0:
            if n & 1:
                return nums2[n // 2]
            else:
                return (nums2[n // 2 - 1] + nums2[n // 2]) / 2.0

        imin, imax, half = 0, m, (m+n+1) // 2
        while imin <= imax:
            i = (imin+imax) // 2
            j = half - i
            if i < imax and nums2[j-1] > nums1[i]:
                imin = i+1
            elif i > imin and nums1[i-1] > nums2[j]:
                imax = i-1
            else:
                if i == 0:
                    max_of_left = nums2[j-1]
                elif j == 0:
                    max_of_left = nums1[i-1]
                else:
                    max_of_left = max(nums1[i-1], nums2[j-1])
                if (m+n) & 1:
                    return max_of_left
                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])
                return (max_of_left + min_of_right) / 2.0