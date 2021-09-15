class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(set)
        visited = defaultdict(lambda: float('inf'))
        for s, e, p in flights:
            graph[s].add((e, p))
        
        queue = deque([(src, -1, 0)])
        while queue:
            pos, curr_k, cost = queue.popleft()
            if pos == dst or curr_k == k: continue
            for neigh, p in graph[pos]:
                if cost + p >= visited[neigh]: continue
                visited[neigh] = cost + p
                queue.append((neigh, curr_k+1, cost + p))
        return visited[dst] if visited[dst] != float('inf') else -1