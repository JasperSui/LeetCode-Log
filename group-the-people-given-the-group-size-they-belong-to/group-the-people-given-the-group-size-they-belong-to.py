class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        res = []
        for i, g in enumerate(groupSizes):
            d[g].append(i)
        for g, people in d.items():
            while people:
                temp = []
                while len(temp) != g:
                    temp.append(people.pop())
                res.append(temp)
        return res
            