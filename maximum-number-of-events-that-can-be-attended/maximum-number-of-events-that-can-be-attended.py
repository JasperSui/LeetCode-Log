class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        pq = []
        res = d = 0
        events.sort(reverse=True)
        while events or pq:
            if not pq: d = events[-1][0]
            while events and events[-1][0] <= d:
                heapq.heappush(pq, events.pop()[1])
            
            heapq.heappop(pq)
            res += 1
            d += 1
            
            while pq and pq[0] < d:
                heapq.heappop(pq)
        return res