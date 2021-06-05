class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col0, m, n = 1, len(matrix), len(matrix[0])
        
        for i in range(m):
            if matrix[i][0] == 0: col0 = 0
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        
        for i in range(m-1, -1, -1):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0 == 0:
                matrix[i][0] = 0
        
        
        # m, n = len(matrix), len(matrix[0])
        # zeros = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 0]
        # true_zeros = set()
        # for i, j in zeros:
        #     for a in range(n):
        #         true_zeros.add((i, a))
        #     for b in range(m):
        #         true_zeros.add((b, j))
        # for i, j in true_zeros:
        #     matrix[i][j] = 0
        