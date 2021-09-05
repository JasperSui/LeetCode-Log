class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        for i in range(1, 10):
            self.dfs(n, str(i), res)
        return res
    
    def dfs(self, n, path, res):
        if int(path) > n: return
        res.append(int(path))
        
        for i in range(10):
            self.dfs(n, path+str(i), res)