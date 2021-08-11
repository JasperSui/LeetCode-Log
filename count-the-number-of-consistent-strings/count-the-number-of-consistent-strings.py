class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return sum(all(c in set(allowed) for c in word) for word in words)