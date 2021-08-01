class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        s, m = sum(milestones), max(milestones)
        if s >= 2 * m:
            return s
        return 2 * (s - m) +1