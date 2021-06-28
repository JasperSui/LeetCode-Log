class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        seen, subtracted = set(), set()
        ans = 0
        for n in nums:
            if n in seen:
                if n not in subtracted:
                    ans -= n
                    subtracted.add(n)
            else:
                ans += n
                seen.add(n)
        return ans