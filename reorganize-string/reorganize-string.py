class Solution:
    def reorganizeString(self, s: str) -> str:
        d = Counter(s)
        res = []
        pq = [(-times, key) for key, times in d.items()]
        heapq.heapify(pq)
        prev_a, prev_b = 0, ''
        while pq:
            a, b = heapq.heappop(pq)
            if prev_a < 0:
                heapq.heappush(pq, (prev_a, prev_b))
            a += 1
            res.append(b)
            prev_a, prev_b = a, b
        if len(res) == len(s): return "".join(res)
        else: return ""