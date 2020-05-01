class Solution:
    def longestPalindrome(self, s):
        res, length = '', 0
        size = len(s)
        if size <= 1:
            return s
        for i in range(size):
            for j in range(size-1, -i, -1):
                if s[j] == s[i]:
                    if j - i + 1 <= length:
                        break
                    if self.isPalindrome(s[i:j+1]):
                        res, length = s[i:j+1], j - i + 1
        return res
    
    def isPalindrome(self, s):
        result = True
        if len(s) == 0:
            return result
        # s = self.cleanString(s)
        if s is None:
            return result
        idx1 = 0
        idx2 = len(s) - 1
        while idx1 < idx2:
            if s[idx1] == s[idx2]:
                idx1 += 1
                idx2 -= 1
            else:
                result = False
                break
        return result
        