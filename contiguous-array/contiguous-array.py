class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count, max_len = 0, 0
        d = {0: 0}
        for index, num in enumerate(nums, 1):
            if num == 0: count -= 1
            else: count += 1
            
            if count in d:
                max_len = max(max_len, index - d[count])
            else:
                d[count] = index
        return max_len