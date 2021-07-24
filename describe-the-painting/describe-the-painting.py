class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        for i, j, c in segments:
            d[i] += c
            d[j] -= c
        res = []
        i = 0
        for j in sorted(d):
            if d[i]:
                res.append([i, j, d[i]])
            d[j] += d[i]
            i = j
        return res