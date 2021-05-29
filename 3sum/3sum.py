class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            front, back = i+1, len(nums)-1
            while front < back:
                s = nums[i] + nums[front] + nums[back]
                if s < 0: front += 1
                elif s > 0: back -= 1
                else:
                    res.append([nums[i], nums[front], nums[back]])
                    while front < back and nums[front] == nums[front+1]: front += 1
                    while front < back and nums[back] == nums[back-1]: back -= 1
                    front += 1
                    back -= 1
        return res
            