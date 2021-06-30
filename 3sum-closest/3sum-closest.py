class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in range(len(nums)-2):
            front, end = i+1, len(nums)-1
            while front < end:
                s = nums[i] + nums[front] + nums[end]
                if s == target: return target
                if abs(target - s) < abs(target - ans):
                    ans = s
                
                if s < target: front += 1
                else: end -= 1
        return ans