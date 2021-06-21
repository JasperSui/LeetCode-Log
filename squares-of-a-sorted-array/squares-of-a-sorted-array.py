class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        l, r = 0, len(nums)-1
        while l <= r:
            ls = abs(nums[l])
            rs = abs(nums[r])
            if ls > rs:
                res.append(ls*ls)
                l += 1
            else:
                res.append(rs*rs)
                r -= 1
        return res[::-1]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        res = []
        l, r = 0, len(nums)-1
        while l <= r:
            ls = abs(nums[l])
            rs = abs(nums[r])
            if ls >= rs:
                res.append(ls*ls)
                l+=1
            else:
                res.append(rs*rs)
                r-=1
        return res[::-1]