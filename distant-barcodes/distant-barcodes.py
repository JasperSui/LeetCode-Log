class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        res, d = [], collections.Counter(barcodes)
        pq = [(-times, num) for num, times in d.items()]
        heapq.heapify(pq)
        prev_a, prev_b = 0, 0
        while pq:
            a, b = heapq.heappop(pq)
            res.append(b)
            if prev_a < 0:
                heapq.heappush(pq, (prev_a, prev_b))
            a += 1
            prev_a, prev_b = a, b
        return res