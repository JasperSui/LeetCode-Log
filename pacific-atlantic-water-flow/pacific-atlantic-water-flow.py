class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        p_visited = [[False for _ in range(n)] for _ in range(m)]
        a_visited = [[False for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            self.dfs(matrix, i, 0, m, n, p_visited)
            self.dfs(matrix, i, n-1, m, n, a_visited)
        
        for j in range(n):
            self.dfs(matrix, 0, j, m, n, p_visited)
            self.dfs(matrix, m-1, j, m, n, a_visited)
        
        res = []
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    res.append([i, j])
        
        return res
    
    def dfs(self, matrix, i, j, m, n, visited):
        visited[i][j] = 1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dir in directions:
            x, y = i + dir[0], j + dir[1]
            if x < 0 or y < 0 or x >= m or y >= n or visited[x][y] or matrix[x][y] < matrix[i][j]: continue
            self.dfs(matrix, x, y, m, n, visited)