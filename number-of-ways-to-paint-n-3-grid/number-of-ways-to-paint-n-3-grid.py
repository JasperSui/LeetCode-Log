class Solution:
    def numOfWays(self, n: int) -> int:
        # https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/discuss/574923/JavaC%2B%2BPython-DP-O(1)-Space
        a121, a123, mod = 6, 6, 10 ** 9 + 7
        for _ in range(n-1):
            a121, a123 = 3*a121+2*a123, 2*a121+2*a123
        return (a121 + a123) % mod