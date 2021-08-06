class Solution:
    def maximum69Number (self, num: int) -> int:
        for i, n in enumerate(str(num)):
            if n == '6':
                return num + 3 * 10 ** (len(str(num)) - i - 1)
        return num