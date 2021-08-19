class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        steps = curr_far = curr_end = 0
        for i in range(len(nums)-1):
            curr_far = max(curr_far, i + nums[i])
            if i == curr_end:
                steps += 1
                curr_end = curr_far
        return steps
        