class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def union(x, y):
            x = find(x)
            y = find(y)
            if x == y: return
            parent[y] = x
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        n = len(stones)
        parent = list(range(1000))
        
        for i in range(n):
            for j in range(i+1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i, j)
        
        ans = 0
        for i in range(n):
            if parent[i] == i:
                ans += 1
        return n - ans
        
        