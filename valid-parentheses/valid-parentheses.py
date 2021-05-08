class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')', '[':']', '{':'}'}
        temp = []
        for c in s:
            if c in d: temp.append(d[c])
            else:
                if not temp or temp.pop() != c: return False
        return True if not temp else False
            