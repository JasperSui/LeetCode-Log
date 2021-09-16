class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        # Two pass
#         n = len(arr)
#         up, down = [0] * n, [0] * n
        
#         for i in range(1, len(arr)):
#             if arr[i] > arr[i-1]:
#                 up[i] = up[i-1] + 1

#         for i in range(len(arr)-2, 0, -1):
#             if arr[i] > arr[i+1]:
#                 down[i] = down[i+1] + 1
        
#         return max([u + d + 1 for u, d in zip(up, down) if u and d] or [0])

        ans = up = down = 0
    
        for i in range(1, len(arr)):
            if down and arr[i-1] < arr[i] or arr[i-1] == arr[i]:
                up = down = 0
            
            up += arr[i-1] < arr[i]
            down += arr[i-1] > arr[i]
            if up and down:
                ans = max(ans, up + down + 1)
        return ans