class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [''] * len(indices)
        for i, x in enumerate(indices):
            result[x] = s[i]
        return ''.join(result)