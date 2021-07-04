class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])
        curr, res = float('-inf'), 0
        for s, e in pairs:
            if curr < s:
                curr, res = e, res+1
        return res