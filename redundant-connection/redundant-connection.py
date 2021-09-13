class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [0] * len(edges)
        
        def find(x):
            if parent[x] == 0:
                return x
            
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            
            if root_x == root_y:
                return False
            
            parent[root_x] = root_y
            return True
        
        for x, y in edges:
            if not union(x-1, y-1):
                return [x, y]
            