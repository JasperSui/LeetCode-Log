class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = float('-inf')
        nums.sort()
        for i in range(len(nums)-2):
            front, end = i+1, len(nums)-1
            while front < end:
                s = nums[front] + nums[i] + nums[end]
                if s == target: return s
                if abs(target - s) < abs(target - ans):
                    ans = s
                if s > target: end -= 1
                else: front += 1
        return ans