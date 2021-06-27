class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [0] * len(edges)
        
        def find(x):
            if parents[x] == 0: return x
            parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return False
            parents[root_x] = root_y
            return True
        
        for x, y in edges:
            if not union(x - 1, y - 1):
                return [x, y]