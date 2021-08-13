class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        brokenLetters = set(brokenLetters)
        return sum(all(c not in brokenLetters for c in word) for word in text.split())