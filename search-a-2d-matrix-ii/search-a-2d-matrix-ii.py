class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        col = len(matrix[0]) - 1
        while col >= 0 and row < len(matrix):
            n = matrix[row][col]
            if n == target:
                return True
            elif n > target:
                col -= 1
            elif n < target:
                row += 1
        return False