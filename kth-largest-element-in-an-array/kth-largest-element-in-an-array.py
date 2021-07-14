class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.quicksort(nums, 0, len(nums)-1)
        return nums[len(nums)-k]
    
    def quicksort(self, nums, l, r):
        if l >= r: return
        pos = self.partition(nums, l, r)
        self.quicksort(nums, l, pos-1)
        self.quicksort(nums, pos+1, r)
    
    def partition(self, nums, l, r):
        pivot = random.randint(l, r)
        nums[pivot], nums[r] = nums[r], nums[pivot]
        for i in range(l, r+1):
            if nums[r] >= nums[i]:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
        return l - 1