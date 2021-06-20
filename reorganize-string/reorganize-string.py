class Solution:
    def reorganizeString(self, s: str) -> str:
        # Max heap
        res, d = [], collections.Counter(s)
        pq = [(-times, char) for char, times in d.items()] # Max heap priority queue
        heapq.heapify(pq)
        prev_a, prev_b = 0, ''
        while pq:
            a, b = heapq.heappop(pq)
            res.append(b)
            if prev_a < 0:
                heapq.heappush(pq, (prev_a, prev_b))
            a += 1 # means -1 for times
            prev_a, prev_b = a, b
        if len(res) != len(s): return ""
        return "".join(res)
        
        
        
        # res = []
        # d = collections.Counter(s)
        # keys = set(d.keys())
        # last = None
        # while len(res) != len(s):
        #     c, _ = max(d.items(), key=lambda x: x[1])
        #     if last != c:
        #         res.append(c)
        #         d[c] -= 1
        #         last = c
        #     else:
        #         max_char, max_count = "", 0
        #         for char in keys - set(c):
        #             if d[char] > max_count:
        #                 max_count = d[char]
        #                 max_char = char
        #         if max_count == 0: return ""
        #         res.append(max_char)
        #         d[max_char] -= 1
        #         last = max_char
        # return "".join(res)