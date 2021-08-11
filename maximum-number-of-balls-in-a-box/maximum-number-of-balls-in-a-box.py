class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d = defaultdict(int)
        for i in range(lowLimit, highLimit+1):
            d[sum(map(int, str(i)))] += 1
        return max(d.values())