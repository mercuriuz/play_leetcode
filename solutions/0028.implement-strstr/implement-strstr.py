class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack is None or needle is None:
            return -1
        if len(needle) == 0:
            return 0
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if self.matchAll(haystack[i:], needle):
                    return i
        return -1

    def matchAll(self, t1, t2):
        if len(t2) > len(t1):
            return False
        for idx in range(len(t2)):
            if t1[idx] != t2[idx]:
                return False
        return True