class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            front, end = i+1, len(nums)-1
            while front < end:
                s = nums[front] + nums[i] + nums[end]
                if s == 0:
                    res.append([nums[front], nums[i], nums[end]])
                    while front < end and nums[front] == nums[front+1]:
                        front += 1
                    while front < end and nums[end] == nums[end-1]:
                        end -= 1
                    
                    front += 1
                    end -= 1
                elif s > 0:
                    end -= 1
                else:
                    front += 1
        return res