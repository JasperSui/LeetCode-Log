class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s: return ""
        rightmost = {c: i for i,c in enumerate(s)}
        res = ""
        for i, c in enumerate(s):
            if c not in res:
                while res and c < res[-1] and i < rightmost[res[-1]]:
                    res = res[:-1]
                res += c
        return res