class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        low, high = 0, m*n-1
        while low < high:
            mid = (low+high) // 2
            if matrix[mid//m][mid%m] == target: return True
            elif matrix[mid//m][mid%m] > target: high = mid
            else: low = mid + 1
        return matrix[low//m][low%m] == target