class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}

        def find(x):
            parent.setdefault(x, x)
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        for x, e, _, y in equations:
            if e == "=":
                union(x, y)
        
        
        for x, e, _, y in equations:
            if e == "!":
                if find(x) == find(y):
                    return False
        return True