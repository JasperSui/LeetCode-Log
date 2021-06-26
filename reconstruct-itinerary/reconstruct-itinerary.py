class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            d[a].append(b)
        
        res = []
        def visit(point):
            while d[point]:
                visit(d[point].pop())
            res.append(point)
        visit('JFK')
        return res[::-1]
            