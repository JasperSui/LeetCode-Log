class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        visited = defaultdict(lambda: float('inf')) # to save the money
        for s, e, p in flights:
            graph[s].append((e, p))
        
        q = deque([(src, -1, 0)])
        while q:
            pos, curr_k, cost = q.popleft()
            if pos == dst or curr_k == k: continue
            for neigh, p in graph[pos]:
                if cost + p >= visited[neigh]: continue
                else:
                    visited[neigh] = cost + p
                    q.append([neigh, curr_k+1, cost+p])
        return visited[dst] if visited[dst] < float('inf') else -1