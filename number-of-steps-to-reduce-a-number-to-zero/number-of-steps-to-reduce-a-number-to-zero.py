class Solution:
    def numberOfSteps(self, num: int) -> int:
        b = f"{num:b}"
        return b.count('1') + len(b) - 1