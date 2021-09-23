class Solution:
    def numberOfSteps(self, num: int) -> int:
        n = str(bin(num)[2:])
        return len(n) + n.count('1') - 1