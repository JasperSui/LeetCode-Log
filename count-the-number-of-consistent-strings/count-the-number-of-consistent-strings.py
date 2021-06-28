class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        def check(s):
            for c in s:
                if not c in allowed:
                    return False
            return True
        return sum([check(word) for word in words])