class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Find the longest decresing suffix
        i = j = len(nums)-1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1
        
        # Reverse if nums is a decreasing list
        if i == 0:
            nums.reverse()
            return
        
        # Pivot
        k = i - 1
        
        # Find the element greater than pivot
        while j > 0 and nums[j] <= nums[k]:
            j -= 1
            
        # Switch
        nums[j], nums[k] = nums[k], nums[j]
        
        # Reverse the rest from k+1 to last element( len(nums)-1 )
        low, high = k+1, len(nums) - 1
        while low < high:
            nums[low], nums[high] = nums[high], nums[low]
            low += 1
            high -= 1