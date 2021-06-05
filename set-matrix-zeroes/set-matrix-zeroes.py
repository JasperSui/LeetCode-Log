class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        zeros = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 0]
        true_zeros = set()
        for i, j in zeros:
            for a in range(n):
                true_zeros.add((i, a))
            for b in range(m):
                true_zeros.add((b, j))
        for i, j in true_zeros:
            matrix[i][j] = 0
        