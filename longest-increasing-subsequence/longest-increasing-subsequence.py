class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            m = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    m = max(m, dp[j] + 1)
            dp[i] = m
        return max(dp)
         
        
        
        
        
        
        
        
        
        
        
        
        
        
        # tails = [0] * len(nums)
        # size = 0
        # for n in nums:
        #     low, high = 0, size
        #     while low < high:
        #         mid = low + (high - low) // 2
        #         if tails[mid] < n:
        #             low = mid + 1
        #         else:
        #             high = mid
        #     tails[low] = n
        #     size = max(size, low+1)
        # return size
        
#         dp = [0] * (len(nums)+1)
#         for i in range(len(nums)):
#             m = 1
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     m = max(m, dp[j] + 1)
            
#             dp[i] = m
#         return max(dp)