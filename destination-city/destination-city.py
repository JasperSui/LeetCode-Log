class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = {}
        for a, b in paths:
            d[a] = b
        
        for a, b in paths:
            if a not in d:
                return a
            if b not in d:
                return b