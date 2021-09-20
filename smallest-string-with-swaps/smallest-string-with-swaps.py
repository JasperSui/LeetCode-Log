class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = list(range(n))
        memo = defaultdict(list)
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        for x, y in pairs:
            union(x, y)
        
        for i in range(n):
            memo[find(i)].append(s[i])
        
        for k in memo:
            memo[k].sort(reverse=True)
        
        res = []
        for i in range(n):
            res.append(memo[find(i)].pop())
        return "".join(res)