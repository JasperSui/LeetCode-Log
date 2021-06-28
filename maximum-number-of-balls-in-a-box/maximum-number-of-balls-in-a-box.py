class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        box = [0] * 46 # 99999
        low, id = lowLimit, 0
        while low > 0:
            id += low % 10
            low //= 10
        
        box[id] += 1
        for i in range(lowLimit+1, highLimit+1):
            while i % 10 == 0:
                id -= 9
                i //= 10
            id += 1
            box[id] += 1
        
        return max(box)
        
        
        # d = defaultdict(int)
        # for i in range(lowLimit, highLimit+1):
        #     num = sum(int(c) for c in str(i))
        #     d[num] += 1
        # return max(d.values())