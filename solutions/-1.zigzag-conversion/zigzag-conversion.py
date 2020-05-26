class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) < numRows or numRows < 2:
            return s
        res, row = [], []
        idx, cnt, forward = 0, 0, True

        while idx < len(s):
            if forward:
                if cnt < numRows:
                    row.append(s[idx])
                    idx += 1
                    cnt += 1
                else:
                    res.append(row)
                    forward = False
            else:
                if cnt > 2:
                    row = [0] * (cnt-2) + [s[idx]] + [0] * (numRows-cnt+1)
                    cnt -= 1
                    idx += 1
                    res.append(row)
                else:
                    row = []
                    cnt = 0
                    forward = True

        if len(row) > 0 and forward:
            row += [0] * (numRows - len(row))
            res.append(row)

        ss = ''
        for col in range(len(res[0])):
            for r in res:
                tmp = r[col]
                ss += tmp if tmp != 0 else ''
        
        return ss