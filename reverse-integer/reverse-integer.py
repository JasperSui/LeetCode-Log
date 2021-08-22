class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        ans = sign * int(str(abs(x))[::-1])
        if -(2**31) <= ans <= (2**31)-1:
            return ans
        return 0