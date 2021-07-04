class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        rows = len(matrix)
        cols = len(matrix[0])
        res = 0
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 1:
                    if r == 0 or c == 0:
                        res += 1
                    else:
                        matrix[r][c] = min(matrix[r-1][c], matrix[r][c-1], matrix[r-1][c-1]) + matrix[r][c]
                        res += matrix[r][c]
        return res