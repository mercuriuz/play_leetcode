MOVES = [
    [0,1,2,3],
    [3,3,2,3],
    [3,3,2,3],
    [3,3,3,3]
]

INT_MIN = -2 ** 31
INT_MAX = 2 ** 31 - 1
class Solution:
    def myAtoi(self, str: str) -> int:
        res, flag = 0, 1
        state = 0
        for c in str:
            idx = self.get_index(c)
            state = MOVES[state][idx]
            if state == 1:
                flag = -1 if c == '-' else 1
            if state == 2:
                res = res * 10 + int(c)
            if res * flag < INT_MIN:
                return INT_MIN
            if res * flag > INT_MAX:
                return INT_MAX
        return res * flag

    def get_index(self, c):
        if c.isspace():
            return 0
        elif c == '-' or c == '+':
            return 1
        elif c.isdigit():
            return 2
        else:
            return 3