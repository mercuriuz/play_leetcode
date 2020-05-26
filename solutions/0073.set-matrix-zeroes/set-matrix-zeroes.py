class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        idx = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    idx.append((i, j))

        while idx:
            i, j = idx.pop()
            matrix[i] = [0] * n
            for k in matrix:
                k[j] = 0