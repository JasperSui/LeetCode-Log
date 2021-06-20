class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            # Make dist negative is becuase we want max heap (python provides only min heap)
            dist = -(x*x + y*y)
            if len(heap) == k:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        return [[x, y] for _, x, y in heap]