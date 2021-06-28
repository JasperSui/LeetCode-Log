class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1 = deque(list(word1))
        word2 = deque(list(word2))
        res = ""
        while word1 or word2:
            if not word2:
                res += word1.popleft()
            elif not word1:
                res += word2.popleft()
            else:
                res += word1.popleft() + word2.popleft()
        return res