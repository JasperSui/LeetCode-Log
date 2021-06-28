class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(c) for c in accounts])