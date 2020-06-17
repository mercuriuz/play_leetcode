class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a, b, p, t = abs(dividend), abs(divisor), 0, 1
        sign = (a == dividend) == (b == divisor)
        if a == 0:
            return 0
        if a == b:
            return 1 if sign else -1
        if b == 1:
            res = a if sign else -a
            return min(res, (1 << 31) - 1)
        if a < b:
            return 0
        while a >= b or t > 1:
            if a >= b:
                p += t
                a -= b
                t <<= 1
                b <<= 1
            else:
                t >>= 1
                b >>= 1
        res = p if sign else -p
        return min(res, (1 << 31) - 1)