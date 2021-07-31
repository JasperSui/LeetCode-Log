class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}
        
        def find(x):
            parent.setdefault(x, x)
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            x = find(x)
            y = find(y)
            if x == y: return
            parent[y] = x
        
        
        
        for eq in equations:
            x, y = eq[0], eq[3]
            if eq[1:3] == "==":
                union(x, y)
        
        for eq in equations:
            x, y = eq[0], eq[3]
            if eq[1:3] == "!=":
                if find(x) == find(y):
                    return False
        
        return True