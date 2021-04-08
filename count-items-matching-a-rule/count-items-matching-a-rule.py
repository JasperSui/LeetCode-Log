class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        m = {"type":0, "color":1, "name":2}
        i = m[ruleKey]
        res = 0
        for a in items:
            if a[i] == ruleValue: res+=1
        return res