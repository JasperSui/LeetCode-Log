class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs(n, 0, 0, "", res)
        return res
    
    def dfs(self, n, open, close, path, res):
        if len(path) == n*2:
            res.append(path)
            return
        
        if open < n:
            self.dfs(n, open+1, close, path + "(", res)
        if close < open:
            self.dfs(n, open, close+1, path + ")", res)