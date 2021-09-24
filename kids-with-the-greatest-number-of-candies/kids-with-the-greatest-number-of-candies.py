class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_c = max(candies)
        return [c + extraCandies >= max_c for c in candies]