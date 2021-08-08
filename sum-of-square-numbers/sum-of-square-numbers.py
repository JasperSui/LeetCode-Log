class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(sqrt(c))
        while left <= right:
            curr = left * left + right * right
            if curr < c:
                left += 1
            elif curr > c:
                right -= 1
            else:
                return True
        return False