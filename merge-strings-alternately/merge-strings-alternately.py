class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        d1 = deque(word1)
        d2 = deque(word2)
        res = ""
        while d1 or d2:
            if not d1:
                res += d2.popleft()
            elif not d2:
                res += d1.popleft()
            else:
                res += d1.popleft() + d2.popleft()
        return res