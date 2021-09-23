class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        i, n = 0, len(events)
        pq = []
        curr_day = 0
        count = 0
        
        while i < n or pq:
            if not pq:
                curr_day = events[i][0]
            
            while i < n and curr_day == events[i][0]:
                heappush(pq, events[i][1])
                i += 1
            
            heappop(pq)
            
            count += 1
            curr_day += 1
            
            while pq and pq[0] < curr_day:
                heappop(pq)
        return count