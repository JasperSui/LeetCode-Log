class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # selection sort
        for i in range(len(nums), len(nums)-k, -1):
            temp = 0
            for j in range(i):
                if nums[j] > nums[temp]:
                    temp = j
            nums[i-1], nums[temp] = nums[temp], nums[i-1]
        return nums[len(nums)-k]