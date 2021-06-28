class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d = defaultdict(int)
        for i in range(lowLimit, highLimit+1):
            num = sum(int(c) for c in str(i))
            d[num] += 1
        return max(d.values())