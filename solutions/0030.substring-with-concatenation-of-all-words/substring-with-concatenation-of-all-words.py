class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        if len(words) > 0:
            if not words[0]:
                return []
        from collections import Counter
        word_map = dict(Counter(words))
        sz = len(words[0])
        cnt = len(words)
        s_sz = len(s)
        res = []
        for i in range(0, s_sz - sz * cnt + 1):
            sub_s = s[i:i+sz*cnt]
            tmp_map = {}
            for j in range(0, sz*cnt, sz):
                tmp = sub_s[j:j+sz]
                if tmp not in words:
                    continue
                tmp_map[tmp] = tmp_map.get(tmp, 0) + 1
                if word_map[tmp] < tmp_map[tmp]:
                    continue
            if word_map == tmp_map:
                res.append(i)
        return res