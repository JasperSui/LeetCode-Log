class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        res = ""
        for word in dictionary:
            data = self.validate(s, word)
            if len(data) > len(res):
                res = data
            elif len(data) == len(res):
                res = min(res, data)
        return res
    
    def validate(self, s, word):
        stack = list(word[::-1])
        for c in s:
            if not stack: break
            if stack[-1] == c:
                stack.pop()
        return "" if stack else word