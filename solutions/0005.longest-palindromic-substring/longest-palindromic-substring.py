class Solution:
    def longestPalindrome(self, s):
        start, length, size = 0, 0, len(s)
        if size <= 1 or s == s[::-1]:
            return s
        for i in range(size):
            if i - length - 1 >= 0 and s[i-length-1:i+1] == s[i-length-1:i+1][::-1]:
                start = i - length - 1
                length += 2
                continue
            if i - length >= 0 and s[i-length:i+1] == s[i-length:i+1][::-1]:
                start = i - length
                length += 1
        return s[start:start+length]