class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0 # m
        col = len(matrix[0])-1 # n
        
        while col >= 0 and row < len(matrix):
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                row += 1
            elif target < matrix[row][col]:
                col -= 1
        return False
                