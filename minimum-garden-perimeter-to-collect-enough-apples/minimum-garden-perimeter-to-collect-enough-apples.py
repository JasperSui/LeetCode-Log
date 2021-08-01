class Solution:
    def minimumPerimeter(self, x: int) -> int:
        low, high = 1, 100000
        ans = 1
        while low < high:
            mid = low + (high - low ) // 2
            if (mid * mid * mid * 4 + mid * mid * 6 + mid * 2) < x:
                low = mid + 1 
            else:
                high = mid
        return low * 8