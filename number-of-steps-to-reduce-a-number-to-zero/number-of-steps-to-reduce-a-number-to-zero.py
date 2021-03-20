class Solution:
    def numberOfSteps (self, num: int) -> int:
        digits = f'{num:b}'
        return digits.count('1') - 1 + len(digits)