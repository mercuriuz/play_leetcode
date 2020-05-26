class Solution:
    def checkRecord(self, s: str) -> bool:
        sz = len(s)
        if sz <= 1:
            return True
        cnta = 0
        cntl = 0
        for idx in range(sz):
            ch = s[idx]
            if ch == 'A':
                cnta += 1
                cntl = 0
            elif ch == 'L':
                cntl += 1
            else:
                cntl = 0
            if cnta == 2 or cntl == 3:
                return False
        return True
    