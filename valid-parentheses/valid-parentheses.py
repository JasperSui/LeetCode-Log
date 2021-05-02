class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {"(": ")", "[": "]", "{": "}"}
        for c in s:
            if c not in d:
                if not stack or c != stack.pop(): return False
            else:
                stack.append(d[c])
        return True if not stack else False