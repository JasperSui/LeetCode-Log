class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = "".join([str(ord(c) - ord('a') + 1) for c in s])
        while k:
            k -= 1
            res = str(sum(map(int, res)))
        return res