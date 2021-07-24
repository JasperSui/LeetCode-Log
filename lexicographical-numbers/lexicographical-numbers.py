class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        for i in range(1, 10):
            self.dfs(i, n, res)
        return res
    
    def dfs(self, curr, n, res):
        if curr > n: return
        res.append(curr)
        for i in range(10):
            if 10 * curr + i > n: return
            self.dfs(10 * curr + i, n , res)