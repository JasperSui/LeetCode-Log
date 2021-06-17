class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        while low < high:
            mid = low + (high - low) // 2
            if sum((p+mid - 1)//mid for p in piles) > h:
                low = mid + 1
            else:
                high = mid
        return low
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Binary Search
        # Time: O(nlog(maxP))
        # Space: O(1)
        low, high = 1, max(piles)
        while low < high:
            mid = (low+high) // 2
            if sum((p+mid)//mid for p in piles) > h:
                low = mid + 1
            else:
                high = mid
        return low
        
        # Shitty try
        # lp = len(piles)
        # piles.sort()
        # if lp <= h < lp*2: return piles[lp-h-1]
        # else:
        #     ans = piles[0]
        #     temp_h = 0
        #     while temp_h != h:
        #         for p in piles:
                    