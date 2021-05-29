class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def find_n_sum(l, r, target, N, result, res):
            if r - l + 1 < N or target < nums[l]*N or target > nums[r]*N: return
            if N == 2:
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        res.append(result + [nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]: l += 1
                        while l < r and nums[r] == nums[r-1]: r -= 1
                        l += 1
                        r -= 1
                    elif s > target:
                        r -= 1
                    else:
                        l += 1
            else:
                for i in range(l, r+1):
                    if i == l or (i > l and nums[i-1] != nums[i]):
                        find_n_sum(i+1, r, target-nums[i], N-1, result+[nums[i]], res)
        
        nums.sort()
        res = []
        find_n_sum(0, len(nums)-1, target, 4, [], res)
        return res