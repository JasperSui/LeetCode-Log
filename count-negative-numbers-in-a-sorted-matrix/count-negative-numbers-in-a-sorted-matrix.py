class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for l in grid:
            low, high = 0, n-1
            while low <= high:
                mid = low + (high - low) // 2
                if l[mid] >= 0:
                    low = mid + 1
                else:
                    high = mid - 1
            ans += n - low
        return ans