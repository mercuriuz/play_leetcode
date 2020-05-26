class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sz = len(s)
        if sz == 0:
            return 0
        curr, cnt = '', 0
        for c in s:
            if c not in curr:
                curr += c
            else:
                curr = curr[curr.find(c)+1:] + c
            if len(curr) > cnt:
                cnt = len(curr)
        return cnt