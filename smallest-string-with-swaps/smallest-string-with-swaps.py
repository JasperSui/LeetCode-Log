class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = list(range(n))
        memo = defaultdict(list)
        
        def union(x, y):
            x = find(x)
            y = find(y)
            if x == y: return
            parent[y] = x
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        res = []
        
        for x, y in pairs:
            union(x, y)
        
        for i in range(n):
            memo[find(i)].append(s[i])
        
        for index in memo.keys():
            memo[index].sort(reverse=True)
        
        for i in range(n):
            res.append(memo[find(i)].pop())

        return "".join(res)