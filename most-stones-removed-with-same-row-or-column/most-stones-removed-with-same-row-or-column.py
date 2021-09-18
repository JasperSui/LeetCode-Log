class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent_count = 0
        n = len(stones)
        parent = list(range(1000))
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        for i in range(n):
            for j in range(1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i, j)
        
        for i in range(n):
            if parent[i] == i:
                parent_count += 1
        
        return n - parent_count