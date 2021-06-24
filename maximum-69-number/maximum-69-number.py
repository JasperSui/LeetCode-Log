class Solution:
    def maximum69Number (self, num: int) -> int:
        ans = num
        s = str(num)
        n = len(s)
        for i in range(n):
            if s[i] == '9': continue
            else:
                ans = max(ans, num + 3 * (10 ** (n - 1 - i)))
        return ans