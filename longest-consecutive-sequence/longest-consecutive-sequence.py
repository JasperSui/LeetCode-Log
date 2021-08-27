class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        d = {}
        for n in nums:
            if n in d: continue
            left = d.get(n-1, 0)
            right = d.get(n+1, 0)
            
            temp_ans = left + right + 1
            d[n] = temp_ans
            ans = max(ans, temp_ans)
            
            d[n-left] = temp_ans
            d[n+right] = temp_ans
        return ans
            
            