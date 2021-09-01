class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.quicksort(nums, 0, len(nums)-1)
        return nums[len(nums)-k]
    
    def quicksort(self, nums, low, high):
        if low > high: return
        pos = self.partition(nums, low, high)
        self.quicksort(nums, low, pos-1)
        self.quicksort(nums, pos+1, high)
    
    def partition(self, nums, low, high):
        pivot = random.randint(low, high)
        nums[pivot], nums[high] = nums[high], nums[pivot]
        for i in range(low, high+1):
            if nums[high] >= nums[i]:
                nums[low], nums[i] = nums[i], nums[low]
                low += 1
        return low - 1
            
            