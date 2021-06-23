class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res = []
        d = defaultdict(list)
        for i, v in enumerate(groupSizes):
            d[v].append(i)
            if len(d[v]) == v:
                res.append(d[v])
                d[v] = []
        return res