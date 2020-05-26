class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        revert = 0
        while revert < x // 10:
            pop = x % 10
            x = x // 10
            revert = revert * 10 + pop
        return revert == x or revert == x // 10