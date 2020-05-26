class Solution:
    def reverse(self, x: int) -> int:
        res, flag = 0, 1
        if x < 0:
            x = -x
            flag = -flag
        while x != 0:
            pop = x % 10
            x = x // 10

            res = res * 10 + pop
            if res * flag < -2 ** 31 or res * flag > 2 ** 31 - 1:
                return 0
        return res * flag