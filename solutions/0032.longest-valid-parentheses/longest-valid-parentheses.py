class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l1, l2, r1, r2, res = 0, 0, 0, 0, 0
        for idx in range(len(s)):
            c1, c2 = s[idx], s[-idx-1]
            if c1 == '(':
                l1 += 1
            else:
                r1 += 1
            if c2 == '(':
                l2 += 1
            else:
                r2 += 1
            
            if l1 == r1:
                res = max(res, 2 * l1)
            elif l1 < r1:
                l1, r1 = 0, 0
            
            if l2 == r2:
                res = max(res, 2 * l2)
            if l2 > r2:
                l2, r2 = 0, 0
        return res