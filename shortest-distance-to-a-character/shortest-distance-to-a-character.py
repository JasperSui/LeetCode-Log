class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n, pos = len(s), float('-inf')
        res = [n] * n
        for i in list(range(n)) + list(range(n))[::-1]:
            if s[i] == c:
                pos = i
            res[i] = min(res[i], abs(i - pos))
        return res