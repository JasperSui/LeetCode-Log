class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        low, high = 1, m*n
        while low < high:
            mid = low + (high-low) // 2
            if sum(min(mid//i, n) for i in range(1, m+1)) < k:
                low = mid + 1
            else:
                high = mid
        return low
        
        
        # low, high = 1, m*n
        # while low < high:
        #     mid = (low+high) // 2
        #     if sum(min(mid//i, n) for i in range(1, m+1)) < k:
        #         low = mid + 1
        #     else: high = mid
        # return low