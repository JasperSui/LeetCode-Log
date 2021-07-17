class Solution:
    def smallestSubsequence(self, s: str) -> str:
        if not s: return ""
        counts = collections.Counter(s)
        pos = 0
        for i, c in enumerate(s):
            if c < s[pos]:
                pos = i
            counts[c] -= 1
            if counts[c] == 0:
                break
        return s[pos] + self.smallestSubsequence(s[pos+1:].replace(s[pos], ""))