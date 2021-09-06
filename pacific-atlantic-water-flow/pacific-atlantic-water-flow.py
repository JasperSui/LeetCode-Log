class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        m, n = len(matrix), len(matrix[0])
        p_visited = [[False for _ in range(n)] for _ in range(m)]
        a_visited = [[False for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            self.dfs(matrix, i, 0, m, n, p_visited, res)
            self.dfs(matrix, i, n-1, m, n, a_visited, res)
        
        for j in range(n):
            self.dfs(matrix, 0, j, m, n, p_visited, res)
            self.dfs(matrix, m-1, j, m, n, a_visited, res)
        
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    res.append([i, j])
        
        return res
    
    def dfs(self, matrix, i, j, m, n, visited, res):
        visited[i][j] = True
        directions = [(1, 0),(-1, 0),(0, 1),(0, -1)]
        for dx, dy in directions:
            x = i + dx
            y = j + dy
            if x < 0 or y < 0 or x >= m or y >= n or visited[x][y] or matrix[x][y] < matrix[i][j]:
                continue
            self.dfs(matrix, x, y, m, n, visited, res)