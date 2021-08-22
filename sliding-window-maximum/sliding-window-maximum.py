class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = [0] * (len(nums) - k + 1)
        right = 0
        q = deque()
        for i in range(len(nums)):
            while q and q[0] < i - k + 1:
                q.popleft()
            
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            
            q.append(i)
            if i - k + 1 >= 0:
                res[right] = nums[q[0]]
                right += 1
        return res