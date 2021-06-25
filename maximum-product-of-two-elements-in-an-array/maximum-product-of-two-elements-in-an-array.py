class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m1 = m2 = float('-inf')
        for n in nums:
            if m1 <= n: m1, m2 = n, m1
            if m1 != n: m2 = max(m2, n)
        return (m1 - 1) * (m2 - 1)
            