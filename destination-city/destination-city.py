class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = {a: b for a, b in paths}
        res = paths[0][1]
        while res in d:
            res = d[res]
        return res