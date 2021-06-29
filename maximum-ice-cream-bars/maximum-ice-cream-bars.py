class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans = 0
        for c in costs:
            if coins >= c:
                ans += 1
                coins -= c
            else:
                break
        return ans