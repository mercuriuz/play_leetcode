class Solution:
    def countAndSay(self, n: int) -> str:
        def process(s):
            res = ''
            cur = s[0]
            cnt = 1
            if len(s) == 1:
                return '11'
            for i in range(1, len(s)):
                if s[i] == cur:
                    cnt += 1
                else:
                    res += '{}{}'.format(cnt, cur)
                    cur = s[i]
                    cnt = 1
            res += '{}{}'.format(cnt, cur)
            return res
    
        rd = 1
        pre, cur = '', '1'
        while rd < n:
            pre, cur = cur, process(cur)
            rd += 1
        return cur