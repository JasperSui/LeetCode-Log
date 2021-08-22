class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse_num(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        if nums:
            k, n = k%len(nums), len(nums)
            reverse_num(0, n-1)
            reverse_num(0, k-1)
            reverse_num(k, n-1)