class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0: 0}
        ans, count = 0, 0
        for index, num in enumerate(nums, 1):
            if num == 0:
                count -= 1
            else:
                count += 1
            
            if count in d:
                ans = max(ans, index - d[count])
            else:
                d[count] = index
        return ans