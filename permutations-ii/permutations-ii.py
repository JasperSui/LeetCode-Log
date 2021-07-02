class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res = [nums]
        temp = nums.copy()
        while 1:
            temp = self.get_next_permutation(temp)
            if temp and temp not in self.res:
                self.res.append(temp.copy())
            else:
                break
        return self.res
    
    def get_next_permutation(self, nums):
        i = j = len(nums)-1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1
        
        if i == 0:
            nums.reverse()
            return nums
        k = i - 1
        
        while j > 0 and nums[j] <= nums[k]:
            j -= 1
        
        nums[j], nums[k] = nums[k], nums[j]
        
        low, high = k+1, len(nums)-1
        while low < high:
            nums[low], nums[high] = nums[high], nums[low]
            low += 1
            high -= 1
        return nums