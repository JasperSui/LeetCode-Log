class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        d = defaultdict(int)
        c = defaultdict(list)
        ans = 0
        for birth, death in logs:
            for i in range(birth, death):
                d[i] += 1
                if d[i] >= ans:
                    heapq.heappush(c[d[i]], i)
                    ans = d[i]
        return heapq.nsmallest(1, c[ans])[0]