class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq = [(row[0], i, 0) for i, row in enumerate(nums)]
        ans = -1e5, 1e5
        heapq.heapify(pq)
        
        right = max(row[0] for row in nums)
        while pq:
            left, i, j = heapq.heappop(pq)
            if right - left < ans[1] - ans[0]:
                ans = left, right
            if j + 1 == len(nums[i]):
                return ans
            v = nums[i][j+1]
            right = max(right, v)
            heapq.heappush(pq, (v, i, j+1))
        