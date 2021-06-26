class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [""] * len(indices)
        for i, x in enumerate(indices):
            res[x] = s[i]
        return "".join(res)