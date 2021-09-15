class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = Counter(s)
        res = ""
        for c in order:
            while c in d and d[c] > 0:
                d[c] -= 1
                res += c
        
        for k, v in d.items():
            res += k * v
        return res