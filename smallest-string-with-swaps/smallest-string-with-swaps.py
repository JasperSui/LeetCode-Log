class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = list(range(n))
        memo = defaultdict(list)
        res = []
        
        def union(x, y):
            parent[find(y)] = find(x)
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        # make x == y's parent
        for x, y in pairs:
            union(x, y)
         
        # find parent of i and append current char into the list
        for i in range(n):
            memo[find(i)].append(s[i])
        
        # Iterate all parent's list and sort them
        for key in memo.keys():
            memo[key].sort(reverse=True)
        
        # Append the smallest char of i's list
        for i in range(n):
            res.append(memo[find(i)].pop())
        
        return "".join(res)
        
            