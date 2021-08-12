class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        d = ["type", "color", "name"]
        n = d.index(ruleKey)
        return len([item for item in items if item[n] == ruleValue])