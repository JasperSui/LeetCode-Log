class Solution:
    def diagonalSort(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        d = defaultdict(list)
        
        for i in range(m):
            for j in range(n):
                d[i - j].append(grid[i][j])
        
        for k in d:
            d[k].sort(reverse=True)
        
        for i in range(m):
            for j in range(n):
                grid[i][j] = d[i - j].pop()
        return grid