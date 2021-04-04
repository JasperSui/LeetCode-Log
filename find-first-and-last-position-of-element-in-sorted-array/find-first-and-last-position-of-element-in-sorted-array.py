class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # O(n) Version
        # m, res = 0, []
        # for i, n in enumerate(nums):
        #     if n == target: 
        #         if not res: res.append(i)
        #         m = max(m, i)
        # if m: res.append(m)
        # if len(res) == 1: res += res
        # return res if res else [-1, -1]
        
        # O(logn) Version
        def get_start_index():
            low, high, index = 0, len(nums)-1, -1
            while low <= high:
                mid = (low+high) // 2
                if nums[mid] == target:
                    index = mid
                    high = mid - 1
                elif nums[mid] > target: high = mid - 1
                else: low = mid + 1
            return index
        
        def get_end_index():
            low, high, index = 0, len(nums)-1, -1
            while low <= high:
                mid = (low+high) // 2
                if nums[mid] == target:
                    index = mid
                    low = mid + 1
                elif nums[mid] > target: high = mid - 1
                else: low = mid + 1
            return index
        
        left, right = get_start_index(), get_end_index()
        if left != -1:
            if right != -1:
                return [left, right]
        return [left, left]