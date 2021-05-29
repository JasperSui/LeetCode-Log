class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a, b = float('inf'), float('inf')
        for i in range(len(nums)-1, -1, -1):
            if i > 0 and nums[i] > nums[i-1]:
                a = i - 1
                break
        if a == float('inf'):
            nums.reverse()
        else:
            for i in range(len(nums)-1, -1, -1):
                if nums[i] > nums[a]:
                    b = i
                    break
            nums[a], nums[b] = nums[b], nums[a]
            l, r = a+1, len(nums)-1
            print(nums)
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1