class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = defaultdict(list)
        for x, y in paths:
            d[x].append(y)
            d[y] = d[y]
        for k, v in d.items():
            if not v: return k