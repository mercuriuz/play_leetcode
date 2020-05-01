class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        row, col = len(A), len(A[0])
        ans = [[None] * row for _ in range(col)]
        for k, v in enumerate(A):
            for k1, v1 in enumerate(v):
                ans[k1][k] = v1
        return ans