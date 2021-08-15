class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        if not arr: return 0
        
        n = len(arr)
        max_of_left = [arr[0]] + [0] * (n-1)
        min_of_right = [0] * (n-1) + [arr[-1]]
        
        for i in range(1, n):
            max_of_left[i] = max(max_of_left[i-1], arr[i])
        
        for i in range(n-2, -1, -1):
            min_of_right[i] = min(min_of_right[i+1], arr[i])
        
        ans = 1
        for i in range(n-1):
            if max_of_left[i] <= min_of_right[i+1]: ans += 1
        return ans