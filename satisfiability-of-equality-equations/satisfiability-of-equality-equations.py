class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}
        
        def union(x, y):
            parent[find(y)] = find(x)
        
        def find(x):
            parent.setdefault(x, x)
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        
        for x, e1, _, y in equations:
            if e1 == "=": union(x, y)
        
        for x, e1, _, y in equations:
            if e1 == "!":
                if find(x) == find(y):
                    return False
        return True