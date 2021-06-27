class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        visited = set()
        for u, v, w in times:
            graph[u].append((v, w))
        
        pq = [(0, k)]
        ans = 0
        
        while pq:
            d, node = heapq.heappop(pq)
            if node in visited: continue
            visited.add(node)
            ans = d
            n -= 1
            for nei, d2 in graph[node]:
                heapq.heappush(pq, (d+d2, nei))
        
        return ans if n == 0 else -1
            