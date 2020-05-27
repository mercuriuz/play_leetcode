class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        n = len(s)
        r2i = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        for idx in range(n-1):
            cur, nxt = r2i[s[idx]], r2i[s[idx+1]]
            if cur < nxt:
                res -= cur
            else:
                res += cur
        return res + r2i[s[-1]]