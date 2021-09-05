class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 按照身高（倒序）和index（順序）排，之後再直接 insert，因為那批高的只會算那批的位置所以不管其他人
        res = []
        for p in sorted(people, key=lambda x: (-x[0], x[1])):
            res.insert(p[1], p)
        return res