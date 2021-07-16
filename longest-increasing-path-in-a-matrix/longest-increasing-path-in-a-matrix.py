class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        d = {}
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                count = 0
                for dx, dy in directions:
                    x = i + dx
                    y = j + dy
                    if 0 <= x <= m-1 and 0 <= y <= n-1 and matrix[x][y] < matrix[i][j]:
                        count += 1
                d[(i, j)] = count
        
        queue = [k for k, v in d.items() if v == 0]
        steps = 0    
        
        while queue:
            new_queue = []
            steps += 1
            for i, j in queue:
                for dx, dy in directions:
                    x = i + dx
                    y = j + dy
                    if 0 <= x <= m-1 and 0 <= y <= n-1 and matrix[x][y] > matrix[i][j] and (x, y) in d:
                        d[(x, y)] -= 1
                        if d[(x, y)] == 0:
                            new_queue.append((x, y))
            queue = new_queue
        return steps
                    