class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        visited = set()
        
        for u, v, w in times:
            graph[u].append((v, w))
        
        pq = [(0, k)]
        while pq:
            delay, node = heapq.heappop(pq)
            if node in visited:
                continue
            visited.add(node)
            ans = delay
            n -= 1
            for neigh, delay_2 in graph[node]:
                heapq.heappush(pq, (delay+delay_2, neigh))
        return ans if n == 0 else -1