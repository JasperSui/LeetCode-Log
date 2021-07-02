class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        steps = curr_far = curr_end = 0
        for i in range(len(nums) - 1):
            curr_far = max(curr_far, i + nums[i])
            if i == curr_end:
                steps += 1
                curr_end = curr_far
        return steps
        
        
        
        
        # target = len(nums)-1
        # step = 0
        # curr_index = 0
        # while curr_index < target:
        #     if curr_index + nums[curr_index] >= target:
        #         step += 1
        #         return step
        #     available_steps = nums[curr_index]
        #     available = nums[curr_index+1:curr_index+1+available_steps]
        #     available = sorted(enumerate(available), reverse=True, key=lambda x: sum(x))
        #     i, _ = available[0]
        #     curr_index += 1 + i
        #     step += 1
        # return step
            
        # if len(nums) <= 1: return 0
        # l, r, step = 0, nums[0], 1
        # while r < len(nums) - 1:
        #     step += 1
        #     next_r = max(i + nums[i] for i in range(l, r+1))
        #     l, r = r, next_r
        # return step
        
        if len(nums) <= 1: return 0
        steps, curr_end, curr_far = 0, 0, 0
        for i in range(len(nums)-1):
            curr_far = max(curr_far, i + nums[i])
            if i == curr_end:
                steps += 1
                curr_end = curr_far
        return steps