class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        allowed = set(list(allowed))
        for word in words:
            ans += 1
            for c in word:
                if c not in allowed:
                    ans -= 1
                    break
        return ans