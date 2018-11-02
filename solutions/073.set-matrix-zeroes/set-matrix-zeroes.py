class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    for k in range(cols):
                        matrix[i][k] = 0 if matrix[i][k] == 0 else 'a'
                    for k in range(rows):
                        matrix[k][j] = 0 if matrix[k][j] == 0 else 'a'
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 'a':
                    matrix[i][j] = 0