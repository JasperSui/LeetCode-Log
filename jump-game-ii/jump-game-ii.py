class Solution:
    def jump(self, nums: List[int]) -> int:
        target = len(nums)-1
        step = 0
        curr_index = 0
        while curr_index < target:
            if curr_index + nums[curr_index] >= target:
                step += 1
                return step
            available_steps = nums[curr_index]
            available = nums[curr_index+1:curr_index+1+available_steps]
            available = sorted(enumerate(available), reverse=True, key=lambda x: sum(x))
            i, _ = available[0]
            curr_index += 1 + i
            step += 1
        return step
            
            