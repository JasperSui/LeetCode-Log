class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        while low < high:
            mid = low + (high - low) // 2
            if sum(math.ceil(p / mid) for p in piles) > h:
                low = mid + 1
            else:
                high = mid
        return low