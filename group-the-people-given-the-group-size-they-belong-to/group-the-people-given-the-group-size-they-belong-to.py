class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        for i, c in enumerate(groupSizes):
            d[c].append(i)
        
        res = []
        for k, l in d.items():
            while d[k]:
                temp = []
                for _ in range(k):
                    temp.append(d[k].pop())
                res.append(temp)
        return res