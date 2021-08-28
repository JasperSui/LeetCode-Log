class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.helper(s, wordDict, {})
    
    def helper(self, s, wordDict, memo):
        if s in memo: return memo[s]
        if not s: return []
        
        res = []
        for word in wordDict:
            if not s.startswith(word): continue
            if len(word) == len(s):
                res.append(word)
            else:
                rest_list = self.helper(s[len(word):], wordDict, memo)
                for item in rest_list:
                    res.append(f"{word} {item}")
        memo[s] = res
        return res