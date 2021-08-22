class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        left = [0] * n
        height = [0] * n
        right = [n] * n
        max_area = 0
        for i in range(m):
            curr_left, curr_right = 0, n
            for j in range(n):
                if matrix[i][j] == "1":
                    left[j] = max(left[j], curr_left)
                    height[j] += 1
                else:
                    left[j] = 0
                    height[j] = 0
                    curr_left = j + 1
                
            for j in range(n-1, -1, -1):
                if matrix[i][j] == "1":
                    right[j] = min(right[j], curr_right)
                    max_area = max(max_area, height[j] * (right[j] - left[j]))
                else:
                    right[j] = n
                    curr_right = j
        return max_area