class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 先排好身高 高的先insert 矮的會在之後insert 所以矮的會在高的前面
        people = sorted(people, key= lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res