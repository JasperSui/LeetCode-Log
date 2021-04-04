class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # O(n) Version
        m, res = 0, []
        for i, n in enumerate(nums):
            if n == target: 
                if not res: res.append(i)
                m = max(m, i)
        if m: res.append(m)
        if len(res) == 1: res += res
        return res if res else [-1, -1]