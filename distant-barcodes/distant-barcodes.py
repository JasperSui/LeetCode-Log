class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        d = Counter(barcodes)
        pq = [(-times, key) for key, times in d.items()]
        heapq.heapify(pq)
        prev_a, prev_b = 0, ""
        res = []
        for _ in range(len(barcodes)):
            a, b = heapq.heappop(pq)
            if prev_a < 0:
                heapq.heappush(pq, (prev_a, prev_b))
            res.append(b)
            a += 1
            prev_a, prev_b = a, b
        return res